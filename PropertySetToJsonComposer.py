import os.path
from PropertyFactory import PropertyFactory
from JsonBuilder import JsonBuilder
from BackendTask import PropertySet
from BackendTask import Property

class PropertySetToJsonComposer(object):

        def doPrint(self, listOfSets, pretty):
                builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
			for propset in listOfSets:
				self.__do(builder, propset)
			builder.closeAll() 
			print builder.build()

                else:
                        print "Empty List, did Nothing"

	def doFile(self, listOfSets, pretty, path):
		builder = JsonBuilder(pretty)
                if (listOfSets is not None and 0 < len(listOfSets)):
			for propset in listOfSets:
				self.__do(builder, propset)
			builder.closeAll()
                        content =  builder.build()

			self.__writeFile(path, content)

                else:
                        print "Empty List, did Nothing"
	
	def __do(self, builder, propset):
		if (isinstance(propset, list)):
                	for pset in propset:
                        	builder.objekt().keyvalue("name", pset.name).keyvalue("type", pset.type).list("properties")
                                for prop in pset.properties:
                                	if (isinstance(prop, list)):
                                        	for pr in prop:
                                                	builder.objekt()
                                                        if (pr.name is not None):
                                                        	builder.keyvalue("name", pr.name)
                                                        if (pr.value is not None):
                                                                builder.keyvalue("value", pr.value)
                                                        if (pr.type is not None):
                                                                builder.keyvalue("type", pr.type)
                                                        builder.close()
                                        else:
                                        	builder.objekt()
                                                if (prop.name is not None):
                                                	builder.keyvalue("name", prop.name)
                                                if (prop.value is not None):
                                                        builder.keyvalue("value", prop.value)
                                                if (prop.type is not None):
                                                        builder.keyvalue("type", prop.type)
                                                builder.close()
				builder.close().close()
		else:
                	builder.objekt().keyvalue("name", propset.name).keyvalue("type", propset.type).list("properties")
                        for prop in propset.properties:
                        	if (isinstance(prop, list)):
                                	for pr in prop:
                                        	builder.objekt()
                                                if (pr.name is not None):
                                                	builder.keyvalue("name", pr.name)
                                                if (pr.value is not None):
                                                        builder.keyvalue("value", pr.value)
                                                if (pr.type is not None):
                                                        builder.keyvalue("type", pr.type)
                                                builder.close()
                                else:
                                	builder.objekt()
                                        if (prop.name is not None):
                                        	builder.keyvalue("name", prop.name)
                                        if (prop.value is not None):
                                                builder.keyvalue("value", prop.value)
                                        if (prop.type is not None):
                                                builder.keyvalue("type", prop.type)
                                        builder.close()
                                builder.close().close()

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
		
