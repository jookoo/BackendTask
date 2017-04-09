class JsonBuilder(object):

	def __init__(self, pretty):
	        self.pretty = pretty
        	self.items = []

	def objekt(self):
		self.items.append(Obj())
		return self

	def keyvalue(self, key, value):
		if (self.items[-1] is None or isinstance(self.items[-1], List)):
			self.items.append(Obj())
		if (isinstance(self.items[-1], KeyValue) or isinstance(self.items[-1], Close)):
			self.items.append(Next())
		self.items[-1].items.append(KeyValue(key,value))			
		return self

	def list(self, key):
		if (self.items[-1] is None):
                        self.items.append(Obj())
		 if (isinstance(self.items[-1], KeyValue) or isinstance(self.items[-1], List) or isinstance(self.items[-1], Close)):
                        self.items.append(Next())
		self.items.append(List(key))
		return self

	def close(self):
		if (self.items[-1] is None):
                        self.items.append(Obj())
		val = ""
		if (isinstance(self.items[-1], List)):
			val = "]"
		else:
			val = "}"
		self.items.append(Close(val))
		return self

	def closeAll(self):
		if (self.items[-1] is None):
                       self.items.append(Obj())
		self.items.append(CloseAll())
		return self
	
	def build(self):
		x = ""
		for item in self.items:
			if (item is not None):
				if (isinstance(item, Obj) or isinstance(item, List)):
					if (isinstance(item, Obj)):
						x = x + "{"
					else:
						if ( 2 < len(x)):
							x = x + ","
							if (self.pretty ==1):
								x = x + "\n"
						
						x = x + "\"" +  item.key + "\": ["
					if (self.pretty == 1):
						x= x + "\n"

					for kv in item.items:
						if(isinstance(kv, KeyValue)):	
							x = x + self.__writekv(len(x), kv.key, kv.value)
						else:			
							index = 2			
							for kvl in kv.items:
								 print index
								 x = x + self.__writekv(index, kvl.key, kvl.value)
								 index = index + 1


					if (self.pretty == 1):
						x = x + "\n" 

				if (isinstance(item, Close)):
                                	x = x + item.value
				
				if (isinstance(item, Next)):
                                        x = x + item.value

				if (isinstance(item, CloseAll)):
					for item in reversed(self.items):
						if (isinstance(item, Obj) or isinstance(item, List)):
							if (self.pretty ==1):
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

	def _classtest(self, cls):
		if(isinstance(cls, KeyValue)):
			return "kv"
		return "list"
			
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

class Next(object):

	def __init__(self):
		self.value = ","

class Close(object):
	
	def __init__(self, value):
		self.value = value

class CloseAll(object):

	def __init__(self):
		self.nothing = 0
