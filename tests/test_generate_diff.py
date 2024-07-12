import pytest
import os

from hexlet_code.gendiff import generate_diff


@pytest.fixture
def test_files(request):
    ext = request.param

    def get_file_path(file_path):
        return os.path.join(os.path.dirname(__file__), 'fixtures', file_path)

    file_path1 = get_file_path(f'file1.{ext}')
    file_path2 = get_file_path(f'file2.{ext}')
    diff_file = get_file_path(f'diff_file_{ext}')
    return file_path1, file_path2, diff_file


@pytest.mark.parametrize('test_files', ['json', 'yaml'], indirect=True)
def test_generate_diff(test_files):
    file_path1, file_path2, diff_file = test_files

    assert open(diff_file).read() == generate_diff(file_path1, file_path2)
