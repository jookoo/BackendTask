from PropertyFactory import PropertyFactory
from JsonBuilder import JsonBuilder

public class PropertySetToJsonComposer(object):

        def doIt(self, listOfSets, pretty):
                builder = JsonBuilder(pretty)

                if (listOfSets is not None and 0 < len(listOfSets)):
                        for propset in listOfSets:
				print propset

                else:
                        print "Empty List, did Nothing"


