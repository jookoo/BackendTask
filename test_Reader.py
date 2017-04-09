import unittest

from Reader import Reader

class Test_test_Reader(unittest.TestCase):

	def test_reader_create(self):
		print "Test zur Erstellung eines Readers"
        	a_reader = Reader("./example_input.py")
		self.assertEquals(a_reader.path, './example_input.py')

	def test_reader_allow_incomplete_off(self):
		print "Test zur Darstellung des Demo-Inputs in einer Objektstruktur, bei der unvollstaendige Properties nicht erlaubt sind"
		a_reader = Reader("./example_input.py")
		a_reader.analyze()
		a_reader.printdata()
		self.assertEquals(len(a_reader.listOfSets), 5)
		for index in range(len(a_reader.listOfSets)):
			propset = a_reader.listOfSets[index]
			if (index == 0):
				self.assertEquals(len(propset.properties), 5)
			else:
				self.assertEquals(len(propset.properties), 4)

		
	def test_reader_allow_incomplete_on(self):
		print "Test zur Darstellung des Demo-Inputs in einer Objektstruktur, bei der unvollstaendige Properties erlaubt sind"
                a_reader = Reader("./example_input.py")
		a_reader.allowIncompleteProperties(1)
                a_reader.analyze()
		a_reader.printdata()
		self.assertEquals(len(a_reader.listOfSets), 5)
		for index in range(len(a_reader.listOfSets)):
                        propset = a_reader.listOfSets[index]
                        self.assertEquals(len(propset.properties), 5)

		
	
if __name__ == '__main__':
    unittest.main()

