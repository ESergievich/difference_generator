from .stylish import stylish_format
from .plain import plain_format


def get_format(diff_file, format_out):
    formats = {
        'stylish': stylish_format(diff_file),
        'plain': plain_format(diff_file),
    }

    return formats[format_out]
