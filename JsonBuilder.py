class JsonBuilder(object):

	def __init__(self, pretty):
	        self.pretty = pretty
        	self.items = []

	def objekt(self):
		self.items.append(Obj())
		return self

	def value(self):
		if (self.__isObjNeed()):
                        self.items.append(Obj())
                if (1 == self.__isNextNeed()):
                        self.items.append(Next())
		self.items.append(Value(value))

	def keyvalue(self, key, value):
		if (self.__isObjNeed()):
			self.items.append(Obj())
		if (1 == self.__isNextNeed()):
			self.items.append(Next())
		self.items.append(KeyValue(key,value))			
		return self

	def list(self, key):
		if (self.__isObjNeed()):
                        self.items.append(Obj())
		if (1 == self.__isNextNeed()):
                        self.items.append(Next())
		self.items.append(List(key))
		return self

	def close(self):
		if (self.__isObjNeed()):
                        self.items.append(Obj())
		val = ""
		if (isinstance(self.items[-1], List)):
			val = "]"
		else:
			val = "}"
		self.items.append(Close(val))
		return self

	def closeAll(self):
		if (self.__isObjNeed()):
                       self.items.append(Obj())
		self.items.append(CloseAll())
		return self
	
	def build(self):
		x = ""
		for item in self.items:
			if (item is not None):
				print item
				if (isinstance(item, Obj)):
					x = x + "{"
					if (self.pretty == 1):
                                	        x= x + "\n"

				if isinstance(item, List):
					if (self.pretty ==1):
						x = x + "\n"
					x = x + "\"" +  item.key + "\": ["
					if (self.pretty == 1):
						x= x + "\n"

				if(isinstance(item, KeyValue)):	
					x = x + self.__writekv(item.key, item.value)

				if(isinstance(item, Value)):
                                        x = x + "\"" +  item.value + "\""

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

	def __writekv(self, key, value):
		x = ""
		if (self.pretty == 1):
                       	x = x + "\n"
                x = x + "\"" + key + "\": \"" + value + "\""
		return x

	def __isObjNeed(self):
		if (0 == len(self.items) or isinstance(self.items[-1], List) or isinstance(self.items[-1], Close)):
			return 1
		return 0
		
	
	def __isNextNeed(self):
		if (isinstance(self.items[-1], Value) or isinstance(self.items[-1], KeyValue)):
			return 1
		return 0

	def _classtest(self, cls):
		if(isinstance(cls, KeyValue)):
			return "kv"
		return "list"
			
class Obj(object):

	def __init__(self):
		self.value = "{"

class Value(object):
	
	def __init__(self, value):
		self.value = value

class KeyValue(object):
	
	def __init__(self, key, value):
		self.key = key
		self.value = value

class List(object):
	
	def __init__(self, key):
		self.key = key
		self.value = "["

class Next(object):

	def __init__(self):
		self.value = ","

class Close(object):
	
	def __init__(self, value):
		self.value = value

class CloseAll(object):

	def __init__(self):
		self.nothing = 0
