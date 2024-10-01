'''
selecting an index from an array where each index has a probability proportional to its weight.
'''

import random
import bisect

class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self):
        target = random.randint(1, self.total_sum)
        # Binary search to find the target zone
        index = bisect.bisect_left(self.prefix_sums, target)
        return index

# Example usage
w = [1, 3, 2]
solution = Solution(w)
print(solution.pickIndex())  # Output could be 0, 1, or 2 with probabilities 1/6, 1/2, and 1/3 respectively
