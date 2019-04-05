import boto3

client1 = boto3.client('s3')
client2 = boto3.client('s3')

def add_my_bucket(params, **kwargs):
	if 'Bucket' not in params:
		params['Bucket'] = 'codeburster'


def add_my_other_bucket(params, **kwargs):
	if 'Bucket' not in params:
		params['Bucket'] = 'hullabulla'

client1.meta.events.register('provide-client-params.s3.ListObjects', add_my_bucket)
client2.meta.events.register('provide-client-params.s3.ListObjects', add_my_other_bucket)

print(client1.list_objects())
print(client2.list_objects())
