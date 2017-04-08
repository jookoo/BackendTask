import unittest

from Reader import Reader

class Test_test_Reader(unittest.TestCase):

	def test_reader_create(self):

        	a_reader = Reader("./example_input.py")
		self.assertEquals(a_reader.path, './example_input.py')

	def test_reader_allow_incomplete_off(self):
		a_reader = Reader("./example_input.py")
		a_reader.analyze()
		a_reader.ausgabe()
		
	def test_reader_allow_incomplete_on(self):
                a_reader = Reader("./example_input.py")
		a_reader.allowIncompleteProperties(1)
                a_reader.analyze()
		a_reader.ausgabe()		
		
	
if __name__ == '__main__':
    unittest.main()

