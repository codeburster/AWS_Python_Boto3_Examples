import boto3
s3 = boto3.client('s3')
response = s3.create_bucket(Bucket='test-87654',CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
print(response)
