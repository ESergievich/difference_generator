import itertools
from .encoder import encoder


def stylish_value(value, depth):
    if isinstance(value, dict):
        string = []
        for k, v in value.items():
            space = '    ' * (depth + 1)
            string.append(f"\n{space}{k}: {stylish_value(v, depth + 1)}")
        s = itertools.chain('{', string, '\n', ['    ' * depth, '}'])
        return ''.join(s)
    else:
        return encoder(value, 'stylish')


def build_string(dictionary, key, depth, sign='  '):
    string = f"{'  ' * depth}{sign}{dictionary['key']}: " \
             f"{stylish_value(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_file):
    def walk(node, depth, replacer='  '):
        space = replacer * (depth + 1)
        diff_result = []
        operations = {
            'nested': lambda v: f"\n{space * 2}{v['key']}: {walk(v['value'], depth + 1)}",
            'unchanged': lambda v: f"\n{space}{build_string(v, 'value', depth)}",
            'changed': lambda v: f"\n{space}{build_string(v, 'old', depth, '- ')}\n"
                                 f"{space}{build_string(v, 'new', depth, '+ ')}",
            'removed': lambda v: f"\n{space}{build_string(v, 'value', depth, '- ')}",
            'added': lambda v: f"\n{space}{build_string(v, 'value', depth, '+ ')}"
        }
        for k, v in node.items():
            diff_result.append(operations[v['operation']](v))
        result = itertools.chain('{', diff_result, '\n', ['    ' * depth + '}'])
        return ''.join(result)

    return walk(diff_file, 0)
