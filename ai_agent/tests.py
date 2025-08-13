import unittest
from functions.get_files_info import get_files_info

class TestGetFiles(unittest.TestCase):
    def testCurrentDir(self):
        result = get_files_info("calculator")
        expected = " - pkg: file_size=4096 bytes, is_dir=True\n - main.py: file_size=565 bytes, is_dir=False\n - tests.py: file_size=1331 bytes, is_dir=False"
        self.assertEqual(result, expected)
        print(result)
    def testPkgDir(self):
        result = get_files_info("calculator", "pkg")
        expected = " - render.py: file_size=754 bytes, is_dir=False\n - calculator.py: file_size=1721 bytes, is_dir=False\n - __pycache__: file_size=4096 bytes, is_dir=True"
        self.assertEqual(result, expected)
        print(result)
    def testNotInDir(self):
        result = get_files_info("calculator", "/bin")
        expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(result, expected)
        print(result)
        result2 = get_files_info("calculator", "../")
        expected2 = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(result2, expected2)
        print(result2)
    def testNotDir(self):
        result = get_files_info("calculator", "main.py")
        expected = 'Error: "main.py" is not a directory'
        self.assertEqual(result, expected)
        print(result)

if __name__ == "__main__":
    unittest.main()