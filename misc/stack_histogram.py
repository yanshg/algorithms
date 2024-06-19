'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height =[2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area =10unit.

For example,

Given heights = [2,1,5,6,2,3],
return 10.
'''

def max_area_in_histogram(heights):
    stack = []

    max_area = 0

    # add -1 in heights to make sure all heights will be pop out and calculated.
    heights += [ -1 ]

    for i, height in enumerate(heights):
        while stack and height < heights[stack[-1]]:
            index = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, heights[index] * width)
        stack.append(i)

    return max_area

heights = [2,1,5,6,2,3]
assert max_area_in_histogram(heights) == 10