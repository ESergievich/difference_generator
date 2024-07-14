from hexlet_code.file_extension import deserialize
from hexlet_code.diff import diff
from hexlet_code.formats.get_format import get_format


def generate_diff(file_path1, file_path2, format_out='stylish'):
    file1 = deserialize(file_path1)
    file2 = deserialize(file_path2)
    diff_file = diff(file1, file2)
    result = get_format(diff_file, format_out)
    return result
