import pytest
import os

from hexlet_code.gendiff import generate_diff


@pytest.fixture
def test_files():
    def get_file_path(filename):
        return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

    file_path1 = get_file_path('file1.json')
    file_path2 = get_file_path('file2.json')
    diff_file = get_file_path('diff_file')
    return file_path1, file_path2, diff_file


def test_generate_diff(test_files):
    file_path1, file_path2, diff_file = test_files

    assert open(diff_file).read() == generate_diff(file_path1, file_path2)
