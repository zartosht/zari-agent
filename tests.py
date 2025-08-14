import unittest

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# class TestGetFilesInfo(unittest.TestCase):
#     def test_calculator_folder(self):
#         result = get_files_info('calculator', ".")
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertIn(" - ", result)
#         self.assertIn("file_size=", result)
#         self.assertIn("is_dir=", result)

#     def test_pkg_folder(self):
#         result = get_files_info('calculator', "pkg")
#         self.assertIsInstance(result, str)
#         self.assertIn(" - ", result)
#         self.assertIn("file_size=", result)
#         self.assertIn("is_dir=", result)

#     def test_calculator_bin(self):
#         result = get_files_info('calculator', "/bin")
#         self.assertIsInstance(result, str)
#         self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

#     def test_relative_url(self):
#         result = get_files_info('calculator', "../")
#         self.assertIsInstance(result, str)
#         self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

# class TestGetFileContent(unittest.TestCase):
#     def test_file_too_large(self):
#         result = get_file_content('calculator', 'lorem.txt')
#         self.assertIsInstance(result, str)
#         self.assertIn("[...File", result)

#     def test_main_py(self):
#         result = get_file_content('calculator', 'main.py')
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertIn("def main(", result)

#     def test_calculator_py(self):
#         result = get_file_content('calculator', 'pkg/calculator.py')
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertIn("def evaluate(", result)

#     def test_file_not_found(self):
#         result = get_file_content('calculator', 'pkg/does_not_exist.py')
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertEqual(result, 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"')

#     def test_outside_permitted_directory(self):
#         result = get_file_content('calculator', '/bin/cat')
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertEqual(result, 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory')

# class TestWriteFile(unittest.TestCase):
#     def test_overwrite_file(self):
#         result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertIn("Successfully wrote to", result)

#     def test_write_file(self):
#         result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertIn("Successfully wrote to", result)

#     def test_write_file_outside_directory(self):
#         result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#         print(result)
#         self.assertIsInstance(result, str)
#         self.assertEqual(result, 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')


class TestRunPythonFile(unittest.TestCase):
    # Update your tests.py file with these test cases, printing each result:
    # run_python_file("calculator", "main.py") (should print the calculator's usage instructions)
    def test_run_main_py(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)

    # run_python_file("calculator", "main.py", ["3 + 5"]) (should run the calculator... which gives a kinda nasty rendered result)
    def test_run_main_py_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        self.assertIsInstance(result, str)

    # run_python_file("calculator", "tests.py")
    def test_run_tests_py(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
        self.assertIsInstance(result, str)

    # run_python_file("calculator", "../main.py") (this should return an error)
    def test_run_main_py_outside_directory(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertIsInstance(result, str)

    # run_python_file("calculator", "nonexistent.py") (this should return an error)
    def test_run_nonexistent_py(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
