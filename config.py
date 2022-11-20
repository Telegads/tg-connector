import os

from dotenv import load_dotenv

load_dotenv()

print(os.environ)

TG_API_ID = os.environ["TG_API_ID"]
TG_API_HASH = os.environ["TG_API_HASH"]

S3_ACCESS_ID = os.environ["S3_ACCESS_ID"]
S3_ACCESS_KEY = os.environ["S3_ACCESS_KEY"]