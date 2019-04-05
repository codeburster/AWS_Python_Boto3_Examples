# 'creating-client-class.service-name'

import boto3

class MyClass(object):
	def __init__(self, *args, **kwargs):
		super(MyClass, self).__init__(*args, **kwargs)
		print("Client class initiated")

def add_custom_class(base_classes, **kwargs):
	base_classes.insert(0,MyClass)


session = boto3.Session()
session.events.register('creating-client-class.s3', add_custom_class)

client123 = session.client('s3')
print(client123)
