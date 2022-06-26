def flatten_dict(data, keystring=''):
    if isinstance(data, dict):
        for key in data:
            new_key = keystring + '_' + key if keystring else key
            yield from flatten_dict(data[key], new_key)
    else:
        yield keystring, data


data = { 'a': { 'b': 'c',  'd': 'e',  'f': { 'g': 'h', 'j': 'k' } },  'i': 'k' }
print(data)

new_data = dict(flatten_dict(data, ''))

print(new_data)
