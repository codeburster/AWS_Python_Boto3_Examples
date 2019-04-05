import boto3
s3 = boto3.client('s3')
for key in s3.list_objects(Bucket='test-87654')['Contents']:
	print(key['Key'])
