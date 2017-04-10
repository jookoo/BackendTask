import unittest

from JsonBuilder import JsonBuilder
from JsonBuilder import KeyValue
from JsonBuilder import List

class Test_test_JsonBuilder(unittest.TestCase):

	def test_builder_create(self):
                a_builder = JsonBuilder(1)
                self.assertEquals(a_builder.pretty, 1)

        def test_builder_classtest(self):
		print "A simple Classmatching Test"
                a_builder = JsonBuilder(0)
                a_keyvalue = KeyValue("a","b")
                a_list = List("a", 0)
                print a_builder._classtest(a_keyvalue)
                print a_builder._classtest(a_list)
		self.assertEquals("kv", a_builder._classtest(a_keyvalue))
		self.assertEquals("list", a_builder._classtest(a_list))

        def test_builder_simple(self):
		print "A simple Builder Test with KeyValues"
                a_builder = JsonBuilder(0)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").close()
		x = a_builder.build()
		self.assertEquals("[{\"a_key\": \"a_value\",\"b_key\": \"b_value\"}]", x)
                print x

        def test_builder_pretty_simple(self):
		print "A simple Builder Test with KeyValues in prittyprint"
                a_builder = JsonBuilder(1)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").close()
		x = a_builder.build()
		self.assertEquals('[{\n    "a_key": "a_value",\n    "b_key": "b_value"\n}]', x)
                print x

        def test_builder_advanced(self):
		print "An advanced Builder Test with KeyValues and Lists"
                a_builder = JsonBuilder(0)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").list("a_list").keyvalue("a_lkey", "alvalue").closeAll()
		x = a_builder.build()
                self.assertEquals('[{"a_key": "a_value","b_key": "b_value","a_list": [{"a_lkey": "alvalue"}]}]', x)
                print x

        def test_builder_pretty_advanced(self):
		print "An advanced Builder Test with KeyValues and Lists in prittyprint"
		a_builder = JsonBuilder(1)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").list("a_list").keyvalue("a_lkey", "alvalue").closeAll()
		x = a_builder.build()
                self.assertEquals('[{\n    "a_key": "a_value",\n    "b_key": "b_value",\n    "a_list": [\n        {\n            "a_lkey": "alvalue"\n        }\n    ]\n}]', x)
                print x
	
	def test_builder_pretty_advanced_close(self):
                print "An advanced Builder Test with KeyValues a List and a Close  in prittyprint"
                a_builder = JsonBuilder(1)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").list("a_list").keyvalue("a_lkey", "alvalue").close().closeAll()
		x = a_builder.build()
                self.assertEquals('[{\n    "a_key": "a_value",\n    "b_key": "b_value",\n    "a_list": [\n        {\n            "a_lkey": "alvalue"\n        }\n    ]\n}]', x)
                print x

	def test_builder_pretty_advanced_multilist_staged_close(self):
                print "An advanced Builder Test with KeyValues and Lists and a Close  in prittyprint"
                a_builder = JsonBuilder(1)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").list("a_list").keyvalue("a_lkey", "alvalue").close().list("b_list").keyvalue("b_lkey","b_lvalue").closeAll()
		x = a_builder.build()
                self.assertEquals('[{\n    "a_key": "a_value",\n    "b_key": "b_value",\n    "a_list": [\n        {\n            "a_lkey": "alvalue"\n        }    ,\n        {\n            "b_list": [\n                {\n                    "b_lkey": "b_lvalue"\n                }\n            ]\n        }\n    ]\n}]', x)
                print x

	def test_builder_pretty_advanced_multilist_two_list_close(self):
                print "An advanced Builder Test with KeyValues and Lists and a double Close  in prittyprint"
                a_builder = JsonBuilder(1)
                a_builder.keyvalue("a_key","a_value").keyvalue("b_key","b_value").list("a_list").keyvalue("a_lkey", "alvalue").close().close().list("b_list").keyvalue("b_lkey","b_lvalue").closeAll()
		x = a_builder.build()
                self.assertEquals('[{\n    "a_key": "a_value",\n    "b_key": "b_value",\n    "a_list": [\n        {\n            "a_lkey": "alvalue"\n        }\n    ],\n    "b_list": [\n        {\n            "b_lkey": "b_lvalue"\n        }\n    ]\n}]', x)
                print x


if __name__ == '__main__':
    unittest.main()


