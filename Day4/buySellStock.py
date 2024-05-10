

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

    
        left = 0  
        max_profit = 0

      
        for right in range(1, len(prices)):
           
            if prices[right] < prices[left]:
                left = right
            current_profit = prices[right] - prices[left]
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
