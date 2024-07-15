from types import NoneType


def encoder(value, format):
    value_encoder = (0, True, False, None)
    json_encoder = {(0, int): 0, (True, bool): 'true', (False, bool): 'false', (None, NoneType): 'null'}
    if value in value_encoder:
        return json_encoder[(value, type(value))]

    if format == 'stylish':
        return value
    if format == 'plain':
        if isinstance(value, int):
            return value
        return f"'{value}'"
