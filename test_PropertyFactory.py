import unittest

from PropertyFactory import PropertyFactory

class Test_test_PropertyFactory(unittest.TestCase):

        def test_factory_create(self):
                print "Test zur Erstellung einer Factory"
		factory = PropertyFactory(0);
                self.assertEquals(factory.allowIncomplete, 0)

        def test_factory_property_create_konsistent(self):
                print "Test zur Erstellung eines Propertyobjekts mit kosistenten Daten"
		factory = PropertyFactory(0);
		keyValues = {"type": "Property", "name": "Width", "value": '100'} 
		properties = factory.createProps(keyValues)
		for prop in properties:
			self.assertEquals(prop.name, "Width")
			self.assertEquals(prop.value, "100")
			self.assertEquals(prop.type, "Property")

if __name__ == '__main__':
    unittest.main()


