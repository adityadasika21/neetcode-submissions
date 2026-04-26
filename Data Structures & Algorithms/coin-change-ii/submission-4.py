class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount +1) for i in range(len(coins)+1)]

        def helper(i, amount): 
            if amount == 0: 
                return 1
            if i >= len(coins): 
                return 0
            if memo[i][amount] != -1: 
                return memo[i][amount]

            res = 0 
         
            if coins[i] <= amount :
                res = helper(i+1, amount)
                res += helper(i, amount - coins[i]) 
                memo[i][amount] = res
            return res

        return helper(0, amount)