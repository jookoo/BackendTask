from BackendTask import PropertySet
from BackendTask import Property

class PropertyFactory(object):

	def __init__(self, allowIncomplete):
		self.allowIncomplete = allowIncomplete
	
	def createSet(self, keyValues):
                a_propertySet = None
                if("name" in keyValues and "type" in keyValues):
                        name = keyValues["name"].replace("\"","")
                        type = keyValues["type"].replace("\"","")
                        if (type == "PropertySet" and name is not None):
                                a_propertySet = PropertySet(name)
                        else:
                                print("Fail: ", name," Set-Data ignored")
                else:
                        print("Set-Data corrupt", keyValues)
                return a_propertySet

	def createProps(self, keyValues):
                x = []
                if("name" in keyValues and "value" in keyValues and "type" in keyValues):
                        name = keyValues["name"].replace("\"","")
                        value = keyValues["value"].replace("\"","")
                        type = keyValues["type"].replace("\"","")
                        if (type == "Property" and name is not None):
                                x.append(Property(name, value))
                        else:
                                print("Fail: ", name," Property-Data ignored")
                else:
                        print("Property corrupt", keyValues)
                return x

	
