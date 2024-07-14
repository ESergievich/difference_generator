import pytest
import os
from hexlet_code.generate_diff import generate_diff


def get_file_path(file_path):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_path)


@pytest.fixture
def test_files(request):
    ext = request.param
    file_path1 = get_file_path(f'file1.{ext}')
    file_path2 = get_file_path(f'file2.{ext}')
    return file_path1, file_path2, ext


@pytest.fixture
def test_diff_file(request):
    ext = request.param
    return get_file_path(f'diff_file_{ext}'), ext


@pytest.mark.parametrize('test_files,test_diff_file',
                         [('json', 'json'), ('yaml', 'yaml'), ('json', 'json_plain'), ('yaml', 'yaml_plain')],
                         indirect=True)
def test_generate_diff(test_files, test_diff_file):
    file_path1, file_path2, in_ext = test_files
    diff_file, exp_ext = test_diff_file

    with open(diff_file, 'r') as diff_f:
        expected_diff = diff_f.read()

    if exp_ext.split('_')[-1] == 'plain':
        assert expected_diff == generate_diff(file_path1, file_path2, 'plain')
    else:
        assert expected_diff == generate_diff(file_path1, file_path2)
