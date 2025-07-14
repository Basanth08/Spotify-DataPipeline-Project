"""
Configuration file for Spotify Data Pipeline Project
This file handles all environment variables and configuration settings
"""

import os
from typing import Optional

class Config:
    """Configuration class for the Spotify Data Pipeline"""
    
    # Spotify API Configuration
    SPOTIFY_CLIENT_ID: Optional[str] = os.environ.get('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET: Optional[str] = os.environ.get('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_PLAYLIST_URL: str = os.environ.get('SPOTIFY_PLAYLIST_URL', 
                                               "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f")
    
    # AWS Configuration
    S3_BUCKET_NAME: Optional[str] = os.environ.get('S3_BUCKET_NAME')
    AWS_REGION: str = os.environ.get('AWS_REGION', 'us-east-1')
    
    # Data Pipeline Configuration
    RAW_DATA_PREFIX: str = "raw_data/to_processed/"
    PROCESSED_DATA_PREFIX: str = "raw_data/processed/"
    TRANSFORMED_DATA_PREFIX: str = "transformed_data/"
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that all required configuration is present"""
        required_vars = [
            'SPOTIFY_CLIENT_ID',
            'SPOTIFY_CLIENT_SECRET', 
            'S3_BUCKET_NAME'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
    
    @classmethod
    def get_spotify_config(cls) -> dict:
        """Get Spotify configuration"""
        cls.validate_config()
        return {
            'client_id': cls.SPOTIFY_CLIENT_ID,
            'client_secret': cls.SPOTIFY_CLIENT_SECRET,
            'playlist_url': cls.SPOTIFY_PLAYLIST_URL
        }
    
    @classmethod
    def get_aws_config(cls) -> dict:
        """Get AWS configuration"""
        cls.validate_config()
        return {
            'bucket_name': cls.S3_BUCKET_NAME,
            'region': cls.AWS_REGION
        } 