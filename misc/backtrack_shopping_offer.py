'''
In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:

Input:
 [2,5], [[3,0,5], [1,2,10]], [3,2]

Output:
 14

Explanation:

There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:

Input:
 [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]

Output:
 11

Explanation:

The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.

Note:

There are at most 6 kinds of items, 100 special offers.

For each item, you need to buy at most 6 of them.

You are not allowed to buy more items than you want, even if that would lower the overall price.

'''

def get_shopping_offers(prices, specials, targets):
    min_cost = float('inf')

    def is_special_applicable(targets, special):
        for t, s in zip(targets, special):
            if t < s:
                return False
        return True
    
    def reduce_target(targets, special):
        return [ t-s for t, s in zip(targets, special)]

    def dfs(prices, specials, targets, costs = []):
        nonlocal min_cost

        is_any_special_applicable = False

        # try each special offer, 
        for special in specials:
            if is_special_applicable(targets, special):
                is_any_special_applicable = True

                special_cost = special[-1]
                costs.append(special_cost)
                dfs(prices, specials, reduce_target(targets, special), costs)
                costs.pop()

        # only when no special offer applicable, calculate the cost
        if not is_any_special_applicable:
            for p, t in zip(prices, targets):
                costs.append(p * t)

            #print("costs: ", costs)
            min_cost = min(min_cost, sum(costs))

    dfs(prices, specials, targets, [])
    return min_cost if min_cost != float('inf') else -1

prices = [2,5]
specials = [[3,0,4], [1,2,10]]
targets = [3,2]
print(get_shopping_offers(prices, specials, targets))

prices = [2,3,4]
specials = [[1,1,0,4],[2,2,1,9]]
targets = [1,2,1]
print(get_shopping_offers(prices, specials, targets))
