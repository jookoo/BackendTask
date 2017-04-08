

class PropertySet(object):

	DEFAULT_TYPE = 'PropertySet'

	def __init__(self, name, *args, **kwargs):
		super(PropertySet, self).__init__(*args, **kwargs)

		self.type = PropertySet.DEFAULT_TYPE
		self.name = name
		self.properties = []
	
	def __repr__(self):
		x = "Type:" + self.type +  " Name:" +  self.name +  " Props:" + str(len(self.properties))
		for prop in self.properties:
			x = x + "\n" + str(prop)
		return x


class Property(object):

	DEFAULT_TYPE = 'Property'

	def __init__(self, name, value, *args, **kwargs):
		super(Property, self).__init__(*args, **kwargs)

		self.type = Property.DEFAULT_TYPE
		self.name = name
		self.value = value

	def __repr__(self):
                return "Type:" + self.type + " Name:" + self.name + " Value:" + str(self.value)

