"""
STATEMENT
Given an array for which the i-th element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell
one share of the stock), find the maximum profit.

CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.
- Is the list sorted? Not necessarily.

EXAMPLES
[7, 1, 5, 3, 6, 4] -> 5 (because 6-1=5)

COMMENTS
- The buying price starts with the first day price.
- We keep store of the profit (which is zero to start with) and update it
  along with the buying price when I get a smaller possible buying price.
- This trick is similar to Kadane's algorithm. In fact, if we convert this array
  to only store the differences between consecutive days, this would transform exactly
  to finding maximum sum subarray.
"""

def maxProfit(prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      if not prices:
          return 0
      max_profit = 0
      buying_price = prices[0]
      for i in range(1, len(prices)):
          if (prices[i]-buying_price > 0):
              max_profit = max(max_profit, prices[i]-buying_price)
          else:
              buying_price = prices[i]
      return max_profit
