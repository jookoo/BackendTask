import unittest

from Reader import Reader

class Test_test_Reader(unittest.TestCase):

    def test_reader_create(self):

        a_reader = Reader("/home/admin/BackendTask/example_input.py")

        self.assertEquals(a_reader.path, '/home/admin/BackendTask/example_input.py')
	a_reader.ausgabe()

if __name__ == '__main__':
    unittest.main()

