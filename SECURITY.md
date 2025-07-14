# Security Guide for Spotify Data Pipeline

## 🔐 Critical Security Measures

### 1. Environment Variables
**NEVER** hardcode credentials in your code. Always use environment variables:

```bash
# ✅ CORRECT - Use environment variables
export SPOTIFY_CLIENT_ID="your_id"
export SPOTIFY_CLIENT_SECRET="your_secret"

# ❌ WRONG - Never hardcode in code
client_id = "c31d09392fae4b60974e22e63ea02085"
```

### 2. AWS Lambda Environment Variables
Set these in your Lambda function configuration:

- `SPOTIFY_CLIENT_ID`
- `SPOTIFY_CLIENT_SECRET`
- `S3_BUCKET_NAME`
- `SPOTIFY_PLAYLIST_URL` (optional)
- `AWS_REGION` (optional)

### 3. IAM Roles and Permissions
Ensure your Lambda functions have minimal required permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
```

### 4. S3 Bucket Security
- Enable server-side encryption
- Use bucket policies to restrict access
- Enable versioning for data protection
- Configure lifecycle policies

### 5. Network Security
- Use VPC for Lambda functions if needed
- Configure security groups appropriately
- Use private subnets for database access

### 6. Monitoring and Logging
- Enable CloudWatch logging
- Set up CloudTrail for API monitoring
- Configure alerts for unusual activity

## 🚨 Security Checklist

Before deploying to production:

- [ ] All credentials moved to environment variables
- [ ] No hardcoded secrets in code
- [ ] IAM roles with minimal permissions
- [ ] S3 bucket encryption enabled
- [ ] CloudWatch logging configured
- [ ] Error handling implemented
- [ ] Input validation added
- [ ] Rate limiting configured
- [ ] Monitoring alerts set up

## 🔍 Security Testing

### Local Testing
```bash
# Test environment variables
python -c "import os; print('SPOTIFY_CLIENT_ID:', bool(os.getenv('SPOTIFY_CLIENT_ID')))"
```

### AWS Security Tools
- AWS Config for compliance monitoring
- AWS Security Hub for security findings
- AWS GuardDuty for threat detection

## 📞 Security Contacts

If you discover a security vulnerability:
1. **DO NOT** create a public issue
2. Contact the maintainer privately
3. Provide detailed reproduction steps
4. Allow time for assessment and fix

## 🔄 Regular Security Updates

- Update dependencies regularly
- Monitor for security advisories
- Rotate credentials periodically
- Review access permissions quarterly 