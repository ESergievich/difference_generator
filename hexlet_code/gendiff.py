import json


def compare(key, file1, file2):
    if key in file1 and key in file2:
        if file1[key] == file2[key]:
            return f"  {key}: {file2[key]}"
        return f"  - {key}: {file1[key]}\n  + {key}: {file2[key]}"
    if key not in file1:
        return f"  + {key}: {file2[key]}"
    return f"  - {key}: {file1[key]}"


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    all_keys = sorted(set(file1.keys() | file2.keys()))
    diff_file = ['{'] + list(map(lambda key, f1=file1, f2=file2: compare(key, f1, f2), all_keys)) + ['}']
    return '\n'.join(diff_file)
