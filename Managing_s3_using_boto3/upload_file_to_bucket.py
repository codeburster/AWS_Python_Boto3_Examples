import boto3

s3 = boto3.client('s3')
res = s3.upload_file('newfile.txt','test-87654','newfile.txt')
print(res)
