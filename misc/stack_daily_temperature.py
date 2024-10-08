'''
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put0instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range[1, 30000]. Each temperature will be an integer in the range[30, 100].

'''

# Monotone Stack

# pop out items that less than current

def get_warmer_temperature(temperatures):
    if not temperatures:
        return []
    
    n = len(temperatures)
    res = [ 0 ] * n
    
    stack = []
    for i, curr_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < curr_temp:
            # pop out the ones whose temperature < curr_temp
            index = stack.pop()
            res[index] = i - index

        stack.append(i)

    # for remaining index in stack, that: res[index] = 0
    # we need not any actions here, since the array was initialized with 0

    return res

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(get_warmer_temperature(temperatures))