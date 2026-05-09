class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        best = 0

        for index, price in enumerate(prices):
            profit = price - prices[buy_index]
            if profit > best:
                best = profit
            elif price < prices[buy_index]:
                buy_index = index

        return best

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