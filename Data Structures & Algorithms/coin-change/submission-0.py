class Solution: 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for currentAmount in range(coin, amount + 1):
                dp[currentAmount] = min(dp[currentAmount], dp[currentAmount - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
                
        
        

        