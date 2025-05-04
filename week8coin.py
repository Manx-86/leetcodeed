class Solution:
    def coinChange(self, denominations: List[int], total: int) -> int:
        if total == 0:
            return 0
        max_val = total + 1
        min_coins = [max_val] * (total + 1)
        min_coins[0] = 0    
        for coin in denominations:
            for current in range(coin, total + 1):
                min_coins[current] = min(min_coins[current], min_coins[current - coin] + 1)      
        return -1 if min_coins[total] == max_val else min_coins[total]
