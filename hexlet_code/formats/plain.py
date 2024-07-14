from .encoder import encoder


def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return encoder(value)


def plain_format(diff_file):
    def walk(node, path):
        operations = {
            'changed': lambda v, p: f"Property '{p}' was updated. "
                                    f"From {plain_value(v['old'])} to {plain_value(v['new'])}",
            'removed': lambda v, p: f"Property '{p}' was removed",
            'added': lambda v, p: f"Property '{p}' was added with value: {plain_value(v['value'])}",
            'nested': lambda v, p: walk(v['value'], p + '.'),
        }
        result = []
        for k, v in node.items():
            if v['operation'] == 'unchanged':
                continue
            current_path = f"{path}{v['key']}"
            result.append(operations[v['operation']](v, current_path))
        return '\n'.join(result)

    return walk(diff_file, '')
