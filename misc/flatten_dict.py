def flatten_dict(data):

    def dfs(data, keys = []):
        if isinstance(data, dict):
            for k, v in data.items():
                yield from dfs(v, keys + [ k ])
        else:
            yield '_'.join(keys), data

    yield from dfs(data, [])


data = { 'a': { 'b': 'c',  'd': 'e',  'f': { 'g': 'h', 'j': 'k' } },  'i': 'k' }
print(data)

new_data = dict(flatten_dict(data))
print(new_data)
