# add a new class to a resource class to inherit from

import boto3

class MyClass(object):
	def __init__(self, *args, **kwargs):
		super(MyClass, self).__init__(*args, **kwargs)
		print("Resource class initiated")

def add_custom_class(base_classes, **kwargs):
	base_classes.insert(0,MyClass)


session = boto3.Session()
session.events.register('creating-resource-class.s3.ServiceResource', add_custom_class)

resource = session.resource('s3')
