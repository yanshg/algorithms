'''
determining the number of groups of similar strings. Two strings are considered similar if they are identical or can be made equivalent by swapping at most two letters within the string. For example, “tars” and “rats” are similar (swapping positions 0 and 2), and “rats” and “arts” are similar, but “star” is not similar to “tars”, “rats”, or "arts"1.
'''

def numSimilarGroups(strs: list[str]) -> int:
    def isSimilar(s1, s2):
        diff = sum([ int(c1 != c2) for c1, c2 in zip(s1, s2)])
        return diff <= 2

    # sink the word
    def dfs(str1, visited):
        visited.add(str1)
        for neighbor in strs:
            if neighbor not in visited and isSimilar(str1, neighbor):
                dfs(neighbor, visited)

    visited = set()
    count = 0
    for str1 in strs:
        if str1 not in visited:
            dfs(str1, visited)
            count += 1
    return count

# Example usage
strs = ["tars", "rats", "arts", "star"]
print(numSimilarGroups(strs))  # Output: 2


