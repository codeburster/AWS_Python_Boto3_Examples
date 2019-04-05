import boto3

s3 = boto3.client('s3')

event_system = s3.meta.events

def add_my_bucket(params, **kwargs):
	if 'Bucket' not in params:
		params['Bucket'] = 'codeburster'


# register the function wo an event (list_objects)
event_system.register('provide-client-params.s3.ListObjects',add_my_bucket)
print(s3.list_objects(Bucket='hullabulla'))
