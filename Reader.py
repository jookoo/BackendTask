import re
import os.path
from BackendTask import PropertySet
from BackendTask import Property
from PropertyFactory import PropertyFactory
class Reader(object):

	RGX_ONE_LINE = "('[a-zA-Z0-9_ {}\":,\.[\]]+')"

	RGX_SPLIT_SET_FROM_PROPS = ":\s+\["

	RGX_SPLIT_PROPS = "({[\":,\s\w\d.\d]+})"

	RGX_KEY_VALUE = "(\"(\w+)\":\s*(\"[a-zA-Z0-9 ]+\"|\d+.{0,1}\d+))"

	DEFAULT_ALLOW_INCOMPLETE_PROP_SETS = 0 
	
	def __init__(self, path):
		self.path = path
		self.listOfSets = []
		self.allowIncomplete = Reader.DEFAULT_ALLOW_INCOMPLETE_PROP_SETS;

	def __readLine(self, part):
		partclean = part.strip()
		p = re.compile(Reader.RGX_ONE_LINE)
		m = p.match(partclean)
		return m

	def __readListOrKeyValue(self, part):
		if (self.__notNoneOrEmpty(part)):
			factory = PropertyFactory(self.allowIncomplete);
			partclean = part.strip()
			basicsplitter = re.compile(Reader.RGX_SPLIT_SET_FROM_PROPS)
			for m in basicsplitter.finditer(partclean):
				setpart = partclean[:m.start()]
				kvs = self.__readKeyValue(setpart)
				propSet = factory.createSet(kvs)
				if (propSet is not None):
					valuepart = partclean[m.start():]
					valuesplitter = re.compile(Reader.RGX_SPLIT_PROPS)
					for n in valuesplitter.finditer(valuepart):
						print n.group(1)
						kvp = self.__readKeyValue(n.group(1))
					        props = factory.createProps(kvp)
						if (props is not None and 0 < len(props)):
							propSet.properties.append(props)
						else:
							print("Properties incomplete, not attached to PropertySet", propSet)
					self.listOfSets.append(propSet)
		else:
			print "Text null or empty"	

	def __readKeyValue(self, part):
		keyValues = {} 
		if (self.__notNoneOrEmpty(part)):
			partclean = part.strip()
			p = re.compile(Reader.RGX_KEY_VALUE)
			for m in p.finditer(partclean):
				if (m is not None  and 0< len(m.groups())):
					key = m.group(2)
					value = m.group(3)
					keyValues[key]=value
		else:
			print "Text null or empty"
		return keyValues

	def __readFile(self):
		if (os.path.exists(self.path)):
			file = open(self.path)
			for line in file:
			    matcher = self.__readLine(line)
			    if (matcher is not None and 0< len(matcher.groups())):
				mline = self.__readListOrKeyValue(matcher.group(1))
	                file.close()
		else:
			print("File not readable", self.path)

	def __notNoneOrEmpty(self,part):
		if (part is not None and 0<len(part) ):
			return True
		return False

	def allowIncompleteProperties(self, value):
		if (value is not None):
			self.allowIncomplete = value
			print ("Incomplete Property Sets allowed = ",value)

	def analyze(self):
		 self.__readFile()

	def ausgabe(self):
		print "--- Data structure ---"
		for propset in self.listOfSets:
			print propset
