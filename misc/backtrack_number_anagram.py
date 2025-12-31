'''
This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.

'''

from collections import Counter

def get_anagram_numbers(s):
    mapping = { '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
    }
    counts_mapping = { c: Counter(mapping[c]) for c in mapping }
    
    def is_contained(counts, num_str_counts):
        for c in num_str_counts:
            if c not in counts or num_str_counts[c] > counts[c]:
                return False
        return True

    def backtrack(counts, res):
        if not counts:
            return res

        for c in mapping:
            if is_contained(counts, counts_mapping[c]):
                result = backtrack(counts - counts_mapping[c], res + c)
                if result:
                    return result
        return ''

    return backtrack(Counter(s), '')
    
s = 'niesevehrtfeev'
print(get_anagram_numbers(s))
