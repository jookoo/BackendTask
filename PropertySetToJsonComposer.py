from PropertyFactory import PropertyFactory
from JsonBuilder import JsonBuilder

class PropertySetToJsonComposer(object):

        def doPrint(self, listOfSets, pretty):
                builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
                        for propset in listOfSets:
				builder.keyvalue("name", propset.name).keyvalue("type",propset.type).list("properties")
				for prop in propset.properties:
					builder.objekt().keyvalue("name",prop.name).keyvalue("value",prop.value).keyvalue("type", prop.type).close()
				builder.closeAll()
				
			print builder.build()

                else:
                        print "Empty List, did Nothing"

	def doFile(self, listOfSets, pretty):
		builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
			for propset in listOfSets:
                                builder.keyvalue("name", propset.name).keyvalue("type",propset.type).list("properties")
                                for prop in propset.properties:
                                        builder.objekt().keyvalue("name",prop.name).keyvalue("value",prop.value).keyvalue("type", prop.type).close()
                                builder.closeAll()

                        print builder.build()

                else:
                        print "Empty List, did Nothing"



