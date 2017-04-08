import unittest

from JsonBuilder import JsonBuilder

class Test_test_JsonBuilder(unittest.TestCase):

        def test_builder_create(self):
                a_builder = JsonBuilder(1)
                self.assertEquals(a_builder.pretty, 1)

	def test_builder_simpel(self):
                a_builder = JsonBuilder(0)
                a_builder.objekt().keyvalue("a_key","a_value").keyvalue("b_key","b_value")
                print a_builder.build()

	
	def test_builder_pretty_simple(self):
		a_builder = JsonBuilder(1)
		a_builder.objekt().keyvalue("a_key","a_value").keyvalue("b_key","b_value")
		print a_builder.build()


if __name__ == '__main__':
    unittest.main()


