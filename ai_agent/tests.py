# import unittest
# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)
'''
def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/tmp.txt", "this should not be allowed")
    print(result)
'''

'''
def test():
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
'''
'''
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
'''
if __name__ == "__main__":
    test()