"""
STATEMENT
Given an array for which the ith element is the price of a given stock on day i, find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

CLARIFICATIONS
- The prices are positive, I assume? Yes.

EXAMPLES
[1,3,2,3] -> 3

COMMENTS
- There is no point to buying and selling at the same day, so we can assume transactions
  happend in different days.
- Starting at the first day, we should go as low as we can to find the buying price, and then
  as high as we can to get the selling price. The difference is added to total profit. We continue
  until we finish the given list.
"""

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    index, profit = 0, 0
    while index < len(prices)-1:
        try:
            while prices[index+1] <= prices[index]:
                index += 1
        except IndexError:
            break

        buying_price = prices[index]
        while index < len(prices)-1 and prices[index+1] >= prices[index]:
            index += 1
        selling_price = prices[index]

        profit += selling_price-buying_price
        index += 1
    return profit
