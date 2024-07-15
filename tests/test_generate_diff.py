import pytest
import os
from gendiff.generate_diff import generate_diff


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
                         [('json', 'json'), ('yaml', 'yaml'), ('json', 'json_fplain'),
                          ('yaml', 'yaml_fplain'), ('json', 'json_fjson')],
                         indirect=True)
def test_generate_diff(test_files, test_diff_file):
    file_path1, file_path2, in_ext = test_files
    diff_file, exp_ext = test_diff_file
    exp_ext = exp_ext.split('_')[-1]

    with open(diff_file, 'r') as diff_f:
        expected_file = diff_f.read()

    received_files = {
        'fplain': generate_diff(file_path1, file_path2, 'plain'),
        'fjson': generate_diff(file_path1, file_path2, 'json')
    }
    received_file = received_files.get(exp_ext, generate_diff(file_path1, file_path2))

    assert expected_file == received_file
