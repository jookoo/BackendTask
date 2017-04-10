import unittest
import hashlib

from Reader import Reader
from PropertySetToJsonComposer import PropertySetToJsonComposer

class Test_test_GesamtDemo(unittest.TestCase):

        PATH_IN = "./example_input.py"

        PATH_OUT = "./demodata/demo_gesamt_pretty.json"

        EXPECTED = "b765a111cc442b85b16f09315e113eca"

        def test_gdemo(self):
                print "Einlesen des Example Input und als Json-Datei schreiben in pretty-Format"
                a_reader = Reader(Test_test_GesamtDemo.PATH_IN)
                a_reader.analyze()
                print a_reader.printdata()
                listOfSets = []
                listOfSets.append(a_reader.getdata())
                composer = PropertySetToJsonComposer()
                composer.doFile(listOfSets, 1, Test_test_GesamtDemo.PATH_OUT)
                actual = hashlib.md5(open(Test_test_GesamtDemo.PATH_OUT, 'rb').read()).hexdigest()
                self.assertEquals(Test_test_GesamtDemo.EXPECTED, actual)

if __name__ == '__main__':
    unittest.main()
