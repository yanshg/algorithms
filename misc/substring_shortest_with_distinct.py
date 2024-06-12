from collections import Counter, defaultdict
def get_shortest_substring(string, chars):

    needs = Counter(chars)
    window = defaultdict(int)
    valid = 0

    shortest_start_index = -1
    shortest_length = len(string)
    
    left = 0
    for right, c in enumerate(string):
        # need NOT check if the character is valid
        window[c] += 1
        if c in needs and window[c] == needs[c]:
            valid += 1

        # when meet the needs then record it and move left
        while left <= right and valid == len(needs):
            l = right - left + 1
            shortest_length = min(shortest_length, l)
            shortest_start_index = left

            lc = string[left]
            if lc in needs and window[lc] == needs[lc]:
                valid -= 1
            window[lc] -= 1

            left += 1

    if shortest_start_index == -1:
        return None

    candidate = string[shortest_start_index: shortest_start_index + shortest_length]
    print("Final smallest substring in ", string, ": ", candidate)
    return candidate


assert get_shortest_substring("figehaeci","aei")== "aeci"
assert get_shortest_substring("figehaeciea","aei")== "iea"
assert not get_shortest_substring("abcdedbc", "gf")
assert get_shortest_substring("abccbbbccbcb", "abc") == "abc"
assert get_shortest_substring("abcdedbc", "db") == "db"
assert get_shortest_substring("abcdedbc", "bc") == "bc"
assert get_shortest_substring("abcdecbd", "bc") == "cb"
assert get_shortest_substring("abcdecdb", "bce") == "ecdb"

