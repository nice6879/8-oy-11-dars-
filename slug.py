ACCESS = "DO003AJMPRNNL3LQAKQ2"
SECRET = "3Pv5qJGUj0SutDYeG9+cwOczCrgRo/1NrTY76v+ksuQ"

import os
import boto3

session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com',
                        aws_access_key_id=ACCESS,
                        aws_secret_access_key=SECRET)

client.upload_file('test.html', 'hello-spaces', 'new-folder/new_file_name.html')