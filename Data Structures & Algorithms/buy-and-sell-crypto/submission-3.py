class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right, price in enumerate(prices):
            if price < prices[left]:
                left = right
            maxProfit = max(maxProfit, price - prices[left])
        
        return maxProfit



"""
given prices list where price[i] is price of stock on day i
can choose a single day to buy and another day to sell

Select the buy and sell day such that profit is maximized, can choose no trasaction, which result in 0 profit


                    r
                   l 
prices = [10,8,7,5,2]

Use sliding window since we are looking for a contingous range where profit is max

Valid Window:
    price[r] > price[l] - then use just compute profit and compare aginst max profit so far

    if price[l] > price[r], means future price greater than price[r] would result in greater profit than buying on day
    l and selling in future. This means moving left pointer to r.

Complexity:
    - O(n) time since we need to loop through prices
    - O(1) aux and output space 
"""