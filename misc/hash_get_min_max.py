'''
This problem was asked by Dropbox.

Create a data structure that performs all the following operations in O(1) time:

plus: Add a key with value 1. If the key already exists, increment its value by one.
minus: Decrement the value of a key. If the key's value is currently 1, remove it.
get_max: Return a key with the highest value.
get_min: Return a key with the lowest value.

'''

class MinMax:
    def __init__(self):
        self.data = {}

        self.max_value = float('-inf')
        self.max_count = 0

        self.min_value = float('inf')
        self.min_count = 0


    def plus(self, key):
        if not key:
            raise ValueError('invalid key')

        v = self.data.get(key, 0) + 1
        self.data[key] = v

        if v < self.min_value:
            self.min_value = v
            self.min_count = 1
        elif v - 1 == self.min_value:
            self.min_count -= 1

        if v > self.max_value:
            self.max_value = v
            self.max_count = 1
        elif v == self.max_value:
            self.max_count += 1

        

    def minus(self, key):
        if not key:
            raise ValueError('invalid key')

        v = self.data.get(key, 0)
        self.data[key] = v - 1


    def get_max(self):
        return max(self.data.values())

    def get_min(self):
        return min(self.data.values())



min_max = MinMax()

min_max.plus('a')
min_max.plus('a')
min_max.plus('b')
min_max.plus('b')
min_max.plus('b')

print("min: ", min_max.get_min())
print("max: ", min_max.get_max())

print(min_max.data)
