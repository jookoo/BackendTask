import unittest

from PropertySetToJsonComposer import PropertySetToJsonComposer
from BackendTask import PropertySet
from BackendTask import Property

class Test_test_PropertyToJsonComposer(unittest.TestCase):

        def test_composer_doprint_empty_list(self):
		print "DoPrint mit einer leeren Liste"
		#doIt(self, listOfSets, pretty):
		listOfSets = []
                a_composer = PropertySetToJsonComposer()
		a_composer.doPrint(listOfSets, 0)
		#self.assertEquals(a_builder.pretty, 1)
	
	def test_composer_doprint_demo_input(self):
                #doIt(self, listOfSets, pretty)
		print "DoPrint Test mit den Bereitgestellten Testdaten"
		property_set = PropertySet('Test Property Set 1')
		property_set.properties.append(Property('Width', 100))
		property_set.properties.append(Property('Height', 100))
		property_set.properties.append(Property('ThermalTransmittance', 0.9))
		property_set.properties.append(Property('FireResistance', 'Class 4'))
		property_set.properties.append(Property('WindLoadRating', 'Class 3'))
                listOfSets = []
		listOfSets.append(property_set)
                a_composer = PropertySetToJsonComposer()
                a_composer.doPrint(listOfSets, 0)
                #self.assertEquals(a_builder.pretty, 1)
	
	def test_composer_doFile_demo_input(self):
                #doIt(self, listOfSets, pretty)
                print "DoFile Test mit den Bereitgestellten Testdaten"
                property_set = PropertySet('Test Property Set 1')
                property_set.properties.append(Property('Width', 100))
                property_set.properties.append(Property('Height', 100))
                property_set.properties.append(Property('ThermalTransmittance', 0.9))
                property_set.properties.append(Property('FireResistance', 'Class 4'))
                property_set.properties.append(Property('WindLoadRating', 'Class 3'))
                listOfSets = []
                listOfSets.append(property_set)
                a_composer = PropertySetToJsonComposer()
                a_composer.doFile(listOfSets, 0)
                #self.assertEquals(a_builder.pretty, 1)



if __name__ == '__main__':
    unittest.main()


