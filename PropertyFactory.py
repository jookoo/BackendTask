from BackendTask import PropertySet
from BackendTask import Property

class PropertyFactory(object):

	def __init__(self, allowIncomplete):
		self.allowIncomplete = allowIncomplete
	
	def createSet(self, keyValues):
                a_propertySet = None
                if("name" in keyValues and "type" in keyValues):
                        name = self.__readValue(keyValues,"name")
                        type = self.__readValue(keyValues,"type")
                        if (type == "PropertySet" and name is not None):
                                a_propertySet = PropertySet(name)
                        else:
                                print("Fail: ", name," Set-Data ignored")
                else:
                        print("Set-Data corrupt", keyValues)
                return a_propertySet

	def createProps(self, keyValues):
                x = []
                if(self.allowIncomplete == 1 or ("name" in keyValues and "value" in keyValues and "type" in keyValues)):
                        name = self.__readValue(keyValues,"name")
                        value = self.__readValue(keyValues,"value")
                        type = self.__readValue(keyValues,"type")
                        if (self.allowIncomplete == 1 or (type == "Property" and self.__checkIsEmpty(name) and self.__checkIsEmpty(value))):
                                x.append(Property(name, value))
                        else:
                                print("Fail: ", name," Property-Data ignored")
                else:
                        print("Property corrupt", keyValues)
                return x

	def __checkIsEmpty(self, value):
		if (value is None or value == ""):
			return true
		return false

	def __readValue(self, keyValues, key):
		if (key in keyValues):
			return keyValues[key].replace("\"","")
		return ""

