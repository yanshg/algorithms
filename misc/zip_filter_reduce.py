'''
L.index(value, [start, [stop]]) -> integer -- return first index of value

Return zero-based index in the list of the first item whose value is equal to x. 
Raises a ValueError if there is no such item.

'''


def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

all_indices("foo", ["foo","bar","baz","foo"])



'''
defaultdict(int)

The function int() which always returns zero is just a special case of constant functions. A faster and more flexible way to create constant functions is to use a lambda function which can supply any constant value (not just zero):

>>>
def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d
'John ran to <missing>'
'''

from collections import defaultdict

# min_eliminations is dict structure with { (y, x): k + 1 }
# initially with { (0,0): 0 }
min_eliminations = defaultdict(lambda: k + 1, {(0,0): 0})
min_eliminations[(0,1)] = 2

'''
Integers and Floating-Point Numbers
The abs() function is one of the built-in functions that are part of the Python language. That means you can start using it right away without importing:
'''


abs(-12)
abs(-12.0)





from collections import Counter

c = Counter(a=2, b=-4)

c = Counter({'a': 2, 'b': -4})

+c
Counter({'a': 2})
-c
Counter({'b': 4})



# must add () for operation << 
depth = 2
(1<<depth) - 1

points = [ (1, 11), (2, 21), (3, 31), (4, 41) ]
xs, ys = list(zip(*points))
print("xs: ", xs, "ys: ", ys)

second_points = list(zip(xs, ys))
print("second_points", second_points)

third_lists = [(1, 2, 3, 4), (11, 21, 31, 41)]
third_points = list(zip(*third_lists))
print("third points:", third_points)


nums = [ 1,  -1,  3,  -3]
negative_nums = list(filter(lambda x: x<0, nums))
print(negative_nums)


s = '1  3'
try:
    f = float(s)
except ValueError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exceptions.")

def is_valid_num_with_re(string):
    return bool(re.match(r'[+-]?\d*\.?\d+([eE][+-]?\d+)?$',string))



SPACE_CHAR = ' '

def init_crypt_data(words):
    crypt_data = dict()

    values = dict()
    chars = list()

    max_len = len(words[-1])
    reversed_words = map(reversed, map(lambda s: s.rjust(max_len), words));
    cols = list(zip(*reversed_words))
    for col in cols:
        for c in col:
            if c != SPACE_CHAR and c not in values:
                values[c] = None
                chars += [c]

    crypt_data['chars'] = chars
    crypt_data['values'] = values
    crypt_data['cols'] = cols
    crypt_data['leading_chars'] = { word[0] for word in words }
    return crypt_data

def is_valid(crypt_data):
    chars = crypt_data['chars']
    values = crypt_data['values']
    cols = crypt_data['cols']
    leading_chars = crypt_data['leading_chars']

    for c in leading_chars:
        if values[c] == 0:
            return False

    carry = 0
    for col in cols:
        value = carry
        l = len(col)
        for i,c in enumerate(col):
            if c == SPACE_CHAR:
                continue

            if values[c] is None:
                return True

            if i < l-1:
                value += values[c]

        if (value % 10) != values[col[-1]]:
            return False

        carry = value // 10

    return True

def solve_puzzle(crypt_data,i,nums):
    chars=crypt_data['chars']
    if i==len(chars):
        return crypt_data['values']

    if not nums:
        return None

    c=chars[i]
    for num in nums:
        crypt_data['values'][c]=num
        if is_valid(crypt_data):
            solution = solve_puzzle(crypt_data,i+1,nums-{num})
            if solution is not None:
                return solution
        crypt_data['values'][c]=None

    return None

def solve_cryptarithmetic(words):
    crypt_data=init_crypt_data(words)
    nums=set(range(10))

    # Starting from the first character to solve
    return solve_puzzle(crypt_data,0,nums)

assert solve_cryptarithmetic(['SEND','MORE','MONEY']) == {'M': 1, 'R': 8, 'D': 7, 'N': 6, 'E': 5, 'S': 9, 'O': 0, 'Y': 2}
assert solve_cryptarithmetic(['CP','IS','FUN','TRUE']) == {'T': 1, 'P': 2, 'R': 0, 'N': 7, 'E': 4, 'U': 8, 'S': 5, 'I': 6, 'C': 3, 'F': 9}




all = []
intervals = [ (1, 2),  (3, 4) ]
for interval in intervals:
    all += [ (interval[0], 1), (interval[1], -1) ]
print(all)
