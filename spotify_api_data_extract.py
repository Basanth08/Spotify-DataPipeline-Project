import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime
from config import Config

def lambda_handler(event, context):
    
    try:
        # Validate configuration
        Config.validate_config()
        
        # Get configuration
        spotify_config = Config.get_spotify_config()
        aws_config = Config.get_aws_config()
        
        client_credentials_manager = SpotifyClientCredentials(
            client_id=spotify_config['client_id'], 
            client_secret=spotify_config['client_secret']
        )
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        playlist_URI = spotify_config['playlist_url'].split("/")[-1].split("?")[0]
        spotify_data = sp.playlist_tracks(playlist_URI)   
        
        client = boto3.client('s3')
        filename = "spotify_raw_" + str(datetime.now()) + ".json"
        
        client.put_object(
            Bucket=aws_config['bucket_name'],
            Key=Config.RAW_DATA_PREFIX + filename,
            Body=json.dumps(spotify_data)
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully extracted data to {filename}')
        }
        
    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Configuration Error: {str(e)}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
