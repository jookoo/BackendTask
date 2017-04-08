class JsonBuilder(object):

	def __init__(self, pretty):
	        self.pretty = pretty
        	self.items = []

	def objekt(self):
		self.items.append(Obj())
		return self

	def keyvalue(self, key, value):
		if (self.items[-1] is None):
			self.items.append(Obj())
		self.items[-1].items.append(KeyValue(key,value))			
		return self

	def list(self, key):
		if (self.items[-1] is None):
                        self.items.append(Obj())
		self.items[-1].items.append(List(key))
		return self

	def build(self):
		x = ""
		for item in self.items:
			if (item is not None):
				if (isinstance(item, Obj)):
					x = "{"
				else:
					x = "["
				if (self.pretty == 1):
					x= x + "\n"

				for kv in item.items:
					if (isinstance(kv, KeyValue)):
						x = x + self.__writekv(len(x),kv.key, kv.value)
					else:
						for kvl in kv.items:
							 x = x + self.__writekv(len(x),kvl.key, kvl.value)


				if (self.pretty == 1):
					x = x + "\n" 

				if (isinstance(item, Obj)):
                                	x = x + "}"
                                else:
                                	x = x + "]"


		return x

	def __writekv(self,lenx, key, value):
		x = ""
		if ( 3 > lenx):
			x = x + "\"" + key + "\": \"" + value + "\""
                else:
			if (self.pretty == 1):
                        	x = x + ",\n"
			else:
				x = x + ","
                        x = x + "\"" + key + "\": \"" + value + "\""
		return x
			
class Obj(object):

	def __init__(self):
		self.items = []

class KeyValue(object):
	
	def __init__(self, key, value):
		self.key = key
		self.value = value

class List(object):
	
	def __init__(self, key):
		self.key = key
		self.items = []
