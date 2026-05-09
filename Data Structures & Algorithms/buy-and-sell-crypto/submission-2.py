class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best_price = 0
        for right, price in enumerate(prices):
            if price < prices[left]:
                left = right
            best_price = max(price - prices[left], best_price)
        return best_price

"""
10 1 5 6 7 1 0 10

buy index = 6
best = 10

profit = 10


loop through all item in list starting at index 0
    profit = value at current index = value at buy index

    if profit > best
        best = profit

    if value at current index < buy index
        buy index = current index


"""