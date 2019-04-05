# to add a custom method to the client class

import boto3

def my_custom_method(self):
	print("this is a custom method")

def add_custom_method_to_client_class(class_attributes, **kwargs):
	class_attributes['my_method'] = my_custom_method


session = boto3.Session()
session.events.register('creating-client-class.s3', add_custom_method_to_client_class)

client = session.client('s3')
client.my_method()
#print(client)
