class JsonBuilder(object):

	PRETTY_DIST = 4		
	
	OPENER_OBJ_START = "{"

	OPENER_LIST_START = "["

	OPENER_OBJ_END = "}"
	
	OPENER_LIST_END = "]"

	VALUE_TAG = "\""

	VALUE_SEPERATOR = ":"

	LINE_FEED = "\n"

	LINE_TAB = "\t"

	SPACE = " "

	def __init__(self, pretty):
	        self.pretty = pretty
		self.level = 0
        	self.items = []

	def objekt(self):
		if (self.__isNextNeed()):
                        self.items.append(Next(0))
		level = self.__findAndRaiseCurrentLevel()
		self.items.append(Obj(level))
		return self

	def list(self, key):
                if (self.__isObjNeed()):
			if (self.__isNextNeed()):
	                        nxtlevel = self.__findCurrentLevel() - 1
        	                self.items.append(Next(nxtlevel))
			level = self.__findAndRaiseCurrentLevel()
                        self.items.append(Obj(level))
                if (self.__isNextNeed()):
			nxtlevel = self.__findCurrentLevel() - 1
                        self.items.append(Next(nxtlevel))
		level = self.__findAndRaiseCurrentLevel()
                self.items.append(List(key, level))
                return self

	def value(self, value):
		if (self.__isObjNeed()):
			if (self.__isNextNeed()):
                                nxtlevel = self.__findCurrentLevel() - 1
                                self.items.append(Next(nxtlevel))
			level = self.__findAndRaiseCurrentLevel()
                        self.items.append(Obj(level))
                if (self.__isNextNeed()):
                        self.items.append(Next(0))
		self.items.append(KeyValue(None,value))
		return self

	def keyvalue(self, key, value):
		if (self.__isObjNeed()):
			if (self.__isNextNeed()):
                                nxtlevel = self.__findCurrentLevel() - 1
                                self.items.append(Next(nxtlevel))
			level = self.__findAndRaiseCurrentLevel()
			self.items.append(Obj(level))
		if (self.__isNextNeed()):
			self.items.append(Next(0))
		self.items.append(KeyValue(key, value))			
		return self

	def close(self):
		closeval = self.__searchLastOpenInstance()
		if (closeval is not None):
			self.items.append(Close(closeval))
		else:
			print "No Open instances, Close was not appended"
		return self

	def closeAll(self):
		closeval = self.__searchLastOpenInstance()
		while closeval is not None:
			self.items.append(Close(closeval))
			closeval = self.__searchLastOpenInstance()
		return self
	
	def build(self):
		x = ""
		for item in self.items:
			if (item is not None):
				if (isinstance(item, Obj)):
					if (self.pretty):
						if (0==len(x)):
	                                                self.level = item.level
						x = x + JsonBuilder.LINE_TAB.expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					x = x + JsonBuilder.OPENER_OBJ_START
					if(self.pretty):
                                		self.level = self.level + 1
			                        x = x + JsonBuilder.LINE_FEED

				if (isinstance(item, List)):
					if (self.pretty):
						x = x + JsonBuilder.LINE_TAB.expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					x = x + JsonBuilder.VALUE_TAG +  item.key + JsonBuilder.VALUE_TAG + JsonBuilder.VALUE_SEPERATOR + JsonBuilder.SPACE +  JsonBuilder.OPENER_LIST_START
					if (self.pretty):
						self.level = self.level + 1
                                                x = x + JsonBuilder.LINE_FEED

				if (isinstance(item, KeyValue)):	
					if (self.pretty):
                                                x = x + JsonBuilder.LINE_TAB.expandtabs(self.level*JsonBuilder.PRETTY_DIST)
					if (item.key is not None and 0 < len(item.key)):
						x = x + JsonBuilder.VALUE_TAG + item.key + JsonBuilder.VALUE_TAG + JsonBuilder.VALUE_SEPERATOR + JsonBuilder.SPACE
					x = x + JsonBuilder.VALUE_TAG + str(item.value) + JsonBuilder.VALUE_TAG

				if (isinstance(item, Close)):
                                        if (self.pretty):
						self.level = self.level - 1
					        x = x + JsonBuilder.LINE_FEED
						x = x + JsonBuilder.LINE_TAB.expandtabs(self.level*JsonBuilder.PRETTY_DIST)
                                	x = x + item.value
				
				if (isinstance(item, Next)):
					if (self.pretty):
                                                x = x + JsonBuilder.LINE_TAB.expandtabs(item.level*JsonBuilder.PRETTY_DIST)
                                        x = x + item.value
					if (self.pretty):
                                                x = x + JsonBuilder.LINE_FEED

				print(item, self.level)
		self.level = 0

		return "[" + x + "]"
	
	def __isObjNeed(self):
		if (0 == len(self.items) or isinstance(self.items[-1], List) or isinstance(self.items[-1], Next)):
			return 1
		if (isinstance(self.items[-1], Close)):
			it = self.__searchLastOpen()
			if (it is not None and isinstance(it, List)):
				return 1
		return 0		
	
	def __isNextNeed(self):
		if (0 < len(self.items) and (isinstance(self.items[-1], KeyValue) or isinstance(self.items[-1], Close))):
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

	def __searchLastOpenInstance(self):
		val = None
		item = self.__searchLastOpen()
		if (item is not None):
	                if (isinstance(item, List)):
        	                val = "]"
                	else:
                        	val = "}"
		return val

	def __searchLastOpen(self):
		worklist = []
                for it in self.items:
                        if (isinstance(it, Obj) or isinstance(it, List)):
                                worklist.append(it)
                        if (isinstance(it, Close)):
                                worklist.pop()

		if (0 < len(worklist)):
			return worklist[-1] 
		return None

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

class KeyValue(object):
	
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Next(object):

	def __init__(self, nxtlevel):
		self.value = ","
		self.level = nxtlevel

class Close(object):
	
	def __init__(self, value):
		self.value = value
