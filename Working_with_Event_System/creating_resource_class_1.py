# add a method to a resource class

import boto3

def custom_method(self):
	print("This is a custom method added to resource class")

def add_custom_method(class_attributes, **kwargs):
	class_attributes['my_function'] = custom_method

session = boto3.Session()

session.events.register('creating-resource-class.s3.ServiceResource', add_custom_method)

resource = session.resource('s3')
resource.my_function()
