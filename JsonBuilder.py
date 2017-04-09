class JsonBuilder(object):

	PRETTY_DIST = 4		

	def __init__(self, pretty):
	        self.pretty = pretty
		self.level = 0
        	self.items = []

	def objekt(self):
		if (self.__isNextNeed()):
                        self.items.append(Next())
		level = self.__findAndRaiseCurrentLevel()
		self.items.append(Obj(level))
		return self

	def list(self, key):
                if (self.__isObjNeed()):
			level = self.__findAndRaiseCurrentLevel()
                        self.items.append(Obj(level))
                if (self.__isNextNeed()):
                        self.items.append(Next())
		level = self.__findAndRaiseCurrentLevel()
                self.items.append(List(key, level))
                return self

	def value(self):
		if (self.__isObjNeed()):
			level = self.__findAndRaiseCurrentLevel()
                        self.items.append(Obj(level))
                if (self.__isNextNeed()):
                        self.items.append(Next())
		self.items.append(Value(value))

	def keyvalue(self, key, value):
		if (self.__isObjNeed()):
			level = self.__findAndRaiseCurrentLevel()
			self.items.append(Obj(level))
		if (self.__isNextNeed()):
			self.items.append(Next())
		self.items.append(KeyValue(key, value))			
		return self

	def close(self):
		if (self.__isObjNeed()):
			level = self.__findAndRaiseCurrentLevel()
                        self.items.append(Obj(level))
		val = ""
		if (isinstance(self.items[-1], List)):
			val = "]"
		else:
			val = "}"
		self.items.append(Close(val))
		return self

	def closeAll(self):
		if (self.__isObjNeed()):
			level = self.__findAndRaiseCurrentLevel()
                       	self.items.append(Obj(level))
		self.items.append(CloseAll())
		return self
	
	def build(self):
		x = ""
		for item in self.items:
			if (item is not None):
				if (isinstance(item, Obj)):
					if (self.pretty):
						if (0==len(x)):
	                                                self.level = item.level
						x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					x = x + "{"
					if(self.pretty):
                                		self.level = self.level + 1
			                        x = x + "\n"


				if isinstance(item, List):
					if (self.pretty):
						x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					x = x + "\"" +  item.key + "\": ["
					if (self.pretty):
						self.level = self.level + 1
                                                x = x + "\n"

				if(isinstance(item, KeyValue)):	
					if (self.pretty):
                                                x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					x = x + "\"" + item.key + "\": \"" + str(item.value) + "\""

				if(isinstance(item, Value)):
                                        if (self.pretty):
                                                x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
                                        x = x + "\"" +  str(item.value) + "\""

				if (isinstance(item, Close)):
                                        if (self.pretty):
						self.level = self.level - 1
					        x = x + "\n"
						x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
                                	x = x + item.value
					if (self.pretty):
                                                x = x + "\n"

				
				if (isinstance(item, Next)):
                                        x = x + item.value
					if (self.pretty):
                                                x = x + "\n"

				if (isinstance(item, CloseAll)):
					ignorenext = 0
					once = 0
					for it in reversed(self.items):
						if (isinstance(it, Close)):
							ignorenext = ignorenext + 1
						if (isinstance(it, Obj) or isinstance(it, List)):
							if (0 < ignorenext):
								ignorenext = ignorenext - 1
							else:
								if (self.pretty):
									self.level = self.level - 1
									# Buggy.... noch fixen
									if(0 == once and (isinstance(self.items[-2], Value) or isinstance(self.items[-2], KeyValue))):
										x = x + "\n"
										once = 1
									x = x + "\t".expandtabs(self.level*JsonBuilder.PRETTY_DIST)
	
								if (isinstance(it, Obj)):
									x = x + "}"
								else:
									x = x + "]"
								if (self.pretty):
                                                                        x = x + "\n"

				print(item, self.level)
		self.level = 0

		return x
	
	def __isObjNeed(self):
		if (0 == len(self.items) or isinstance(self.items[-1], List) or isinstance(self.items[-1], Next)):
			return 1
		return 0		
	
	def __isNextNeed(self):
		if (isinstance(self.items[-1], Value) or isinstance(self.items[-1], KeyValue) or isinstance(self.items[-1], Close)):
			return 1
		return 0

	def __findAndRaiseCurrentLevel(self):
		return self.__findCurrentLevel() + 1

	def __findCurrentLevel(self):
		if (0 == len(self.items)):
			return -1
		else:
			level = 0
			for item in self.items:
				if (isinstance(item, List) or isinstance(item, Obj)):
					level = level + 1
				if (isinstance(item, Close)):
					level = level - 1
			return level

	def _classtest(self, cls):
		if(isinstance(cls, KeyValue)):
			return "kv"
		return "list"
			
class Obj(object):

	def __init__(self, level):
		self.level = level
		self.value = "{"

class List(object):

        def __init__(self, key, level):
		self.level = level
                self.key = key
                self.value = "["

class Value(object):
	
	def __init__(self, value):
		self.value = value

class KeyValue(object):
	
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Next(object):

	def __init__(self):
		self.value = ","

class Close(object):
	
	def __init__(self, value):
		self.value = value

class CloseAll(object):

	def __init__(self):
		self.nothing = 0
