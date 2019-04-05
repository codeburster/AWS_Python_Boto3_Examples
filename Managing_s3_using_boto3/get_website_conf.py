import boto3

# ceate s3 client
s3 = boto3.client('s3')

# retrieve the policies for the bucket
response = s3.get_bucket_website(Bucket='codeburster')
print(response)
