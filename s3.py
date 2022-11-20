import boto3
from botocore.client import Config
import config

BUCKET_NAME = "cb53441-ae878e23-a11b-47c0-91ac-26c03f0731d4"
ENDPOINT = "https://s3.timeweb.com"



def uploadToS3(FILE_NAME):
    s3 = boto3.client(
      's3',
      endpoint_url=ENDPOINT,
      region_name='ru-1',
      aws_access_key_id=config.S3_ACCESS_ID,
      aws_secret_access_key=config.S3_ACCESS_KEY,
      config=Config(s3={'addressing_style': 'path'})
    )

    s3.upload_file(Filename=FILE_NAME, Bucket=BUCKET_NAME, Key=FILE_NAME)

    result_file_path = f"{ENDPOINT}/{BUCKET_NAME}/{FILE_NAME}"

    return result_file_path