import unittest

from Reader import Reader
from PropertySetToJsonComposer import PropertySetToJsonComposer

class Test_test_GesamtDemo(unittest.TestCase):

        def test_gdemo(self):
                print "Einlesen des Example Input und als Json-Datei schreiben in pretty-Format"
                a_reader = Reader("./example_input.py")
		a_reader.analyze()
		print a_reader.printdata()
		listOfSets = []
                listOfSets.append(a_reader.getdata())
		composer = PropertySetToJsonComposer()
		composer.doFile(listOfSets, 1, "./demodata/demo_gesamt_pretty.json")

if __name__ == '__main__':
    unittest.main()

