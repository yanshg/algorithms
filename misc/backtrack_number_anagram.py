'''
This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.

'''

from collections import Counter

def get_anagram_numbers(s):
    mapping = { 0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                }
    
    def is_contained(counts, num_str_counts):
        for c in num_str_counts:
            if c not in counts or num_str_counts[c] > counts[c]:
                return False
        return True

    def backtrack(counts, path = []):
        if not counts:
            #return ''.join(map(str,sorted(path)))
            return ''.join(map(str,path))
        
        for num, num_str in mapping.items():
            num_counts = Counter(num_str)
            if is_contained(counts, num_counts):
                path.append(num)
                res = backtrack(counts - num_counts, path)
                if res:
                    return res
                path.pop()
    
    counts = Counter(s)
    return backtrack(counts, [])
    
s = 'niesevehrtfeev'
print(get_anagram_numbers(s))