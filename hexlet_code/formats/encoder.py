def encoder(value):
    value_encoder = (True, False, None)
    json_encoder = {True: 'true', False: 'false', None: 'null'}
    if value in value_encoder:
        return json_encoder[value]
    return value
