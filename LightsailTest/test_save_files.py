import unittest
import save_files
import sys

class TestSaveFiles(unittest.TestCase):

    def test_create_file(self):
        filename = "sugar"
        actual = save_files.create_file(filename)
        theoretical = {'Done': 1}
        self.assertEqual(actual, theoretical)

    def test_read_file(self):
        filename = "sugar"
        actual = save_files.read_file(filename)
        content = ""
        theoretical = {'content': content}
        self.assertEqual(actual, theoretical)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main(exit=True)

