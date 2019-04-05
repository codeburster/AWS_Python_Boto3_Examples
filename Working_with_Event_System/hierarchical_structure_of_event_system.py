import boto3
s3 = boto3.client('s3')
event_system = s3.meta.events

# general.something.specific
# general.something
# general

def add_general_bucket(params, **kwargs):
	if 'Bucket' not in params:
		params['Bucket'] = 'hullabulla'

def add_specific_bucket(params, **kwargs):
	if 'Bucket' not in params:
		params['Bucket'] = 'codeburster'

event_system.register('provide-client-params.s3', add_general_bucket)
event_system.register('provide-client-params.s3.ListObjects', add_specific_bucket)

list_objects_response = s3.list_objects()
print(list_objects_response)

put_obj_res = s3.put_object(Key='mykey', Body=b'hey there')
print(put_obj_res)
