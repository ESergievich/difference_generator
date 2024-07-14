import json


def json_value(diff_file):
    if isinstance(diff_file, dict):
        return {k: json_value(v) for k, v in diff_file.items()}
    return None if diff_file == '' else diff_file


def json_format(diff_result):
    return json.dumps(json_value(diff_result))
