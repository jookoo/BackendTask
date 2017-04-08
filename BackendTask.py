

class PropertySet(object):

	DEFAULT_TYPE = 'PropertySet'

	def __init__(self, name, *args, **kwargs):
		super(PropertySet, self).__init__(*args, **kwargs)

		self.type = PropertySet.DEFAULT_TYPE
		self.name = name
		self.properties = []
	
	def __str__(self):
		return "Type:" + self.type +  " Name:" +  self.name +  " Props:" + len(self.properties)


class Property(object):

	DEFAULT_TYPE = 'Property'

	def __init__(self, name, value, *args, **kwargs):
		super(Property, self).__init__(*args, **kwargs)

		self.type = Property.DEFAULT_TYPE
		self.name = name
		self.value = value

	def __str__(self):
                return "Type:" + self.type + " Name:" + self.name

