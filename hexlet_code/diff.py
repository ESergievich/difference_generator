def diff(file1, file2):
    """Рекурсивно проходит по ключам двух файлов и сравнивает их."""
    rm_keys = file1.keys() - file2.keys()
    add_keys = file2.keys() - file1.keys()
    all_keys = sorted(file1.keys() | file2.keys())
    diff_file = {}

    for key in all_keys:
        if key in rm_keys:
            description = {'key': key, 'operation': 'removed', 'value': file1[key]}
        elif key in add_keys:
            description = {'key': key, 'operation': 'added', 'value': file2[key]}
        elif file1[key] == file2[key]:
            description = {'key': key, 'operation': 'unchanged', 'value': file1[key]}
        elif all([file1[key] != file2[key], isinstance(file1[key], dict), isinstance(file2[key], dict)]):
            description = {'key': key, 'operation': 'nested', 'value': diff(file1[key], file2[key])}
        else:
            description = {'key': key, 'operation': 'changed', 'old': file1[key], 'new': file2[key]}
        diff_file[key] = description

    return diff_file
