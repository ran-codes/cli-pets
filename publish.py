from dotenv import load_dotenv
import os
import subprocess

## Load secrets from .env file
load_dotenv()
print(os.environ.get('UV_PUBLISH_USERNAME'))
print(os.environ.get('UV_PUBLISH_PASSWORD'))


## Publish using uv
subprocess.run(["uv", "publish"], check=True)