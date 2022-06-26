class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # f(coins, amount) = min(1+f(amount-coin)) for coin in coins
        # top down with memo
        def min_coin_changes(coins,amount,memo):
            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]

            res = float('inf')
            for n in coins:
                res = min(res, 1 + min_coin_changes(coins, amount - n, memo))
            memo[amount] = res
            return res

        memo = dict()
        memo[0] = 0
        min_coin_changes(coins,amount,memo)
        if amount in memo and memo[amount] != float('inf'):
            return memo[amount]
        return -1


    def coinChange_dp(self, coins, amount):

        # DP[i] means min coin changes for i amount
        # DP[0] = 0
        # DP[i] = min (1 + DP[i-c]) for c in coins if c <= i;
        # result: DP[amount] or DP[-1]

        DP = [0] + [ float('inf') ] * amount
        for c in coins:
            for i in range(c, amount+1):
                DP[i] = min(DP[i], 1 + DP[i-c])
        return DP[-1] if DP[-1] != float('inf') else -1

solution=Solution()

assert solution.coinChange([2], 3) == -1
assert solution.coinChange([1,2,5], 20) == 4

assert solution.coinChange_dp([2], 3) == -1
assert solution.coinChange_dp([1,2,5], 20) == 4

