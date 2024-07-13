from hexlet_code.file_extension import deserialize


def custom_json(func):
    """Декоратор для обработки специальных значений JSON."""

    def inner(key, file1, file2, ind, dp):
        json_encoder = {True: 'true', False: 'false', None: 'null'}
        if file1.get(key, 'good_key') in tuple(json_encoder):
            file1[key] = json_encoder.get(file1.get(key))
        if file2.get(key, 'good_key') in tuple(json_encoder):
            file2[key] = json_encoder.get(file2.get(key))
        return func(key, file1, file2, ind, dp)

    return inner


@custom_json
def compare(key, file1, file2, ind, dp):
    """Сравнивает значения по ключу в двух файлах."""
    if key in file1 and key in file2:
        if file1[key] == file2[key]:
            return f"{ind * dp}    {key}: {file2[key]}"
        return f"{ind * dp}  - {key}: {file1[key]}\n{ind * dp}  + {key}: {file2[key]}"
    if key not in file1:
        return f"{ind * dp}  + {key}: {file2[key]}"
    return f"{ind * dp}  - {key}: {file1[key]}"


def format_dict(d, ind, dp):
    """Форматирует словарь для вывода."""
    lines = ["{"]
    for key, value in d.items():
        if isinstance(value, dict):
            lines.append(f"{ind * (dp + 2)}{key}: {format_dict(value, ind, dp + 1)}")
        else:
            lines.append(f"{ind * (dp + 2)}{key}: {value}")
    lines.append(f"{ind * (dp + 1)}}}")
    return '\n'.join(lines)


def walk(file1, file2, ind, dp=0):
    """Рекурсивно проходит по ключам двух файлов и сравнивает их."""
    all_keys = sorted(set(file1.keys() | file2.keys()))
    diff_file = ["{"]
    for key in all_keys:
        if isinstance(file1.get(key, None), dict) and isinstance(file2.get(key, None), dict):
            diff_file.append(f"{ind * (dp + 1)}{key}: {walk(file1.get(key, {}), file2.get(key, {}), ind, dp + 1)}")
        elif isinstance(file1.get(key, None), dict):
            diff_file.append(f"{ind * dp}  - {key}: {format_dict(file1[key], ind, dp)}")
            if file2.get(key, None):
                diff_file.append(f"{ind * dp}  + {key}: {file2[key]}")
        elif isinstance(file2.get(key, None), dict):
            if file1.get(key, None):
                diff_file.append(f"{ind * dp}  - {key}: {file1[key]}")
            diff_file.append(f"{ind * dp}  + {key}: {format_dict(file2[key], ind, dp)}")
        else:
            diff_file.append(compare(key, file1, file2, ind, dp))
    diff_file.append(f"{ind * dp}}}")
    return '\n'.join(diff_file)


def generate_diff(file_path1, file_path2, indent='    '):
    file1 = deserialize(file_path1)
    file2 = deserialize(file_path2)
    return walk(file1, file2, indent)
