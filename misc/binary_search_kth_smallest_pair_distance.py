'''
Find k-th smallest pair distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 
'''

'''
Idea:

Steps
Sort the Array:

Sorting the array simplifies the calculation of pair distances because the distance between two numbers is minimized when they are close in value.
Binary Search on the Distance:

Perform binary search on the range of distances, from 
0
0 to 
𝑚
𝑎
𝑥
(
𝑛
𝑢
𝑚
𝑠
)
−
𝑚
𝑖
𝑛
(
𝑛
𝑢
𝑚
𝑠
)
max(nums)−min(nums).
For a given middle value (mid), determine how many pairs have a distance less than or equal to mid.
Count Pairs with Two Pointers:

Use two pointers to count the number of pairs with a distance ≤ mid efficiently in 
𝑂
(
𝑛
)
O(n) time for a fixed mid.
Adjust Search Range:

If the count of pairs with a distance ≤ mid is at least 
𝑘
k, reduce the search range to find a smaller distance.
Otherwise, increase the search range.

'''

class Solution:
    def smallestDistancePair(self, nums, k):
        def countPairs(max_distance):
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_distance:
                    j += 1
                count += j - i - 1
            return count
        
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Binary search on the distance
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if countPairs(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left

