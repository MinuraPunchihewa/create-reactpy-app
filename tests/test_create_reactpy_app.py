import os
import unittest
from click.testing import CliRunner
from create_reactpy_app.__main__ import main


class TestCreateReactPyApp(unittest.TestCase):
    def test_create_reactpy_app_creates_correct_files_and_directories_with_flask_backend(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(main, ['test_project'])

            # Print the paths of all files and directories in the current directory
            for dirpath, dirnames, filenames in os.walk('.'):
                for dirname in dirnames:
                    print(os.path.join(dirpath, dirname))
                for filename in filenames:
                    print(os.path.join(dirpath, filename))

            with open('test_project/requirements.txt') as f:
                requirements = f.read()
            assert 'reactpy[flask]' in requirements

    def test_create_reactpy_app_creates_correct_files_and_directories_with_starlette_backend(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(main, ['test_project', '--backend', 'starlette'])

            # Print the paths of all files and directories in the current directory
            for dirpath, dirnames, filenames in os.walk('.'):
                for dirname in dirnames:
                    print(os.path.join(dirpath, dirname))
                for filename in filenames:
                    print(os.path.join(dirpath, filename))

            with open('test_project/requirements.txt') as f:
                requirements = f.read()
            assert 'reactpy[starlette]' in requirements

    def test_create_reactpy_app_creates_correct_files_and_directories_with_fastapi_backend(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(main, ['test_project', '--backend', 'fastapi'])

            # Print the paths of all files and directories in the current directory
            for dirpath, dirnames, filenames in os.walk('.'):
                for dirname in dirnames:
                    print(os.path.join(dirpath, dirname))
                for filename in filenames:
                    print(os.path.join(dirpath, filename))

            with open('test_project/requirements.txt') as f:
                requirements = f.read()
            assert 'reactpy[fastapi]' in requirements


if __name__ == '__main__':
    unittest.main()