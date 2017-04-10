import os.path
from PropertyFactory import PropertyFactory
from JsonBuilder import JsonBuilder

class PropertySetToJsonComposer(object):

        def doPrint(self, listOfSets, pretty):
                builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
                        for propset in listOfSets:
				builder.keyvalue("name", propset.name).keyvalue("type", propset.type).list("properties")
				for prop in propset.properties:
                                        builder.objekt()
                                        if (prop.name is not None):
                                                builder.keyvalue("name", prop.name)
                                        if (prop.value is not None):
                                                builder.keyvalue("value", prop.value)
                                        if (prop.type is not None):
                                                builder.keyvalue("type", prop.type)
                                        builder.close()
				builder.closeAll()
				
			print builder.build()

                else:
                        print "Empty List, did Nothing"

	def doFile(self, listOfSets, pretty, path):
		builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
			for propset in listOfSets:
                                builder.objekt().keyvalue("name", propset.name).keyvalue("type", propset.type).list("properties")
                                for prop in propset.properties:
					for str in prop:
						builder.objekt()
        	                                if (str.name is not None):
                	                                builder.keyvalue("name", str.name)
                        	                if (str.value is not None):
                                	                builder.keyvalue("value", str.value)
                                        	if (str.type is not None):
                                                	builder.keyvalue("type", str.type)
                                        	builder.close()
				builder.close().close()
                        builder.closeAll()

                        content =  builder.build()

			self.__writeFile(path, content)

                else:
                        print "Empty List, did Nothing"

	def __writeFile(self, path, content):
		if (path is not None and content is not None):
			parent = os.path.abspath(os.path.join(path, os.pardir))
			if (os.path.exists(parent)):		
				fobj_out = open(path,"w")
				for line in content:
				    fobj_out.write(line)
				fobj_out.close()
			else:
				print "Target-Dir Missing, did Nothing"
		else:
			print "Arguments Missing, did Nothing"
		
