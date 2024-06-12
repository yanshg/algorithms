def flatten_dict(data, keys=[]):
    if isinstance(data, dict):
        for key in data:
            keys.append(key)
            yield from flatten_dict(data[key], keys)
            keys.pop()
    else:
        keystring = '_'.join(keys)
        yield keystring, data


data = { 'a': { 'b': 'c',  'd': 'e',  'f': { 'g': 'h', 'j': 'k' } },  'i': 'k' }
print(data)

new_data = dict(flatten_dict(data))
print(new_data)
