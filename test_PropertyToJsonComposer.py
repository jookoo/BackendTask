import unittest
import hashlib

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
		a_composer.doFile(listOfSets, 0, "./demodata/demo_md5.json")
		actual = hashlib.md5(open("./demodata/demo_md5.json", 'rb').read()).hexdigest()
                self.assertEquals("5ce5fe11238323764e8d9c81d736310d", actual)
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
                a_composer.doFile(listOfSets, 0, "./demodata/demo.json")
		actual = hashlib.md5(open("./demodata/demo.json", 'rb').read()).hexdigest()
                self.assertEquals("5ce5fe11238323764e8d9c81d736310d", actual)
                #self.assertEquals(a_builder.pretty, 1)

	def test_composer_doFile_demo_input_pretty(self):
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
                a_composer.doFile(listOfSets, 1, "./demodata/demo_pretty.json")
		actual = hashlib.md5(open("./demodata/demo_pretty.json", 'rb').read()).hexdigest()
                self.assertEquals("500fa32457f264fc2e32129b31f7e944", actual)
                #self.assertEquals(a_builder.pretty, 1)

	def test_composer_doPrint_empty(self):
		print "DoPrint Test mit leeren Daten"
		a_composer = PropertySetToJsonComposer()
		a_composer.doPrint(None, 0)


if __name__ == '__main__':
    unittest.main()


