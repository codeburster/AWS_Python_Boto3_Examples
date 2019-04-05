import boto3
s3 = boto3.client('s3')

# create website configuration
website_configuration = {
	'ErrorDocument': {'Key': 'error.html'},
	'IndexDocument': {'Suffix': 'index.html'}
}

s3.put_bucket_website(Bucket='codeburster',WebsiteConfiguration=website_configuration)
