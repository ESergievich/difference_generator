import os
import json
import yaml
from yaml.loader import SafeLoader

EXT = {
    ('.json',): lambda file_path: json.load(open(file_path)),
    ('.yml', '.yaml'): lambda file_path: yaml.load(open(file_path), Loader=SafeLoader)
}


def get_file_extension(file_path):
    """Получает расширение файла."""
    _, extension = os.path.splitext(file_path)
    return extension


def deserialize(file_path):
    """Десериализует файл в зависимости от его расширения."""
    extension = get_file_extension(file_path)
    for ext in EXT:
        if extension in ext:
            return EXT[ext](file_path)
