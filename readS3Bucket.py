import boto3
from createTempFile import create_temp_file

s3_resource = boto3.resource('s3')
session = boto3.session.Session()
current_region = session.region_name
bucket_name = input('Enter the bucket name: ')
'''bucket_response = s3_resource.create_bucket(Bucket=bucket_name)
print(bucket_name, current_region)'''

first_file_name = "input.txt"
#Upload a file to S3
first_bucket = s3_resource.Bucket(name=bucket_name)
first_object = s3_resource.Object(
    bucket_name=bucket_name, key="input/"+first_file_name)
'''first_object.upload_file(first_file_name)
s3_resource.Bucket(bucket_name).upload_file(
    Filename=first_file_name, Key="bucket/"+first_file_name)'''
# Download a file from S3
s3_resource.Object(bucket_name, "bucket/"+first_file_name).download_file(
    f'E:\Work Documents\Python\Kafka-python\{first_file_name}')
