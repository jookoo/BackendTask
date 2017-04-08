import re
import os.path
from BackendTask import PropertySet
from BackendTask import Property
from PropertyFactory import PropertyFactory
class Reader(object):

	ALLOW_INCOMPLETE_SETS = 0 
	
	def __init__(self, path):
		self.path = path
		self.listOfSets = []
		self.factory = PropertyFactory(Reader.ALLOW_INCOMPLETE_SETS);

	def __readLine(self, part):
		partclean = part.strip()
		p = re.compile("('[a-zA-Z0-9_ {}\":,\.[\]]+')")
		m = p.match(partclean)
		return m

	def __readListOrKeyValue(self, part):
		if (self.__notNoneOrEmpty(part)):
			partclean = part.strip()
			basicsplitter = re.compile(":\s+\[")
			for m in basicsplitter.finditer(partclean):
				setpart = partclean[:m.start()]
				kvs = self.__readKeyValue(setpart)
				propSet = self.factory.createSet(kvs)
				if (propSet is not None):
					valuepart = partclean[m.start():]
					valuesplitter = re.compile("({[\":,\s\w\d.\d]+})")
					for n in valuesplitter.finditer(valuepart):
						print("valuegroup",n.group(1))
						kvp = self.__readKeyValue(n.group(1))
					        props = self.factory.createProps(kvp)
						if (props is not None and 0 < len(props)):
							propSet.properties.append(props)
						else:
							print("Properties Missing, PropertySet ignored", propSet)
		else:
			print "Text null or empty"	

	def __readKeyValue(self, part):
		keyValues = {} 
		if (self.__notNoneOrEmpty(part)):
			partclean = part.strip()
			p = re.compile("(\"(\w+)\":\s*(\"[a-zA-Z0-9 ]+\"|\d+.{0,1}\d+))")
			for m in p.finditer(partclean):
				if (m is not None  and 0< len(m.groups())):
					key = m.group(2)
					value = m.group(3)
					keyValues[key]=value
		else:
			print "Text null or empty"
		return keyValues

	def __readFile(self):
                file = open(self.path)
		if (file is not None and os.path.exists(self.path)):
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

	def ausgabe(self):
		self.__readFile()
		return self.path
