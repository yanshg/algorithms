'''
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

Output: [20,24]

Explanation:

List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:

The given list may contain duplicates, so ascending order means >= here.

1 <=k<= 3500

-10^5 <=value of elements<= 10^5.

'''

from collections import defaultdict

def get_smallest_range(lists):
    # use num_index_list
    num_index_list = []
    for i,nums in enumerate(lists):
        num_index_list += [ (n, i) for n in nums ]

    num_index_list.sort()
    print(num_index_list)

    res = []
    l = len(lists)

    count = 0
    window = defaultdict(int)

    left = 0
    for right, (n, i) in enumerate(num_index_list):
        c = str(i)
        window[c] += 1
        if window[c] == 1:
            count += 1

        # move left if all lists included
        while left < right and count == l:
            # update left num and right num
            left_num = num_index_list[left][0]
            right_num = num_index_list[right][0]
            if not res or (res[1] - res[0] > right_num - left_num):
                res = [left_num, right_num]

            lc = str(num_index_list[left][1])
            if window[lc] == 1:
                count -= 1
            window[lc] -= 1
            left += 1

    return res


lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(get_smallest_range(lists))