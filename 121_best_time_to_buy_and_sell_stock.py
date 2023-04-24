"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate over the list
        # hold two pointers, left and right
        # left points to the buy date, right points to possible sell dates
        # record the best profit you can get after each buy
        # return the best option

        # edge case for only one day
        if len(prices) == 1:
            return 0

        left = 0
        right = 1
        best_profit = 0
        while right < len(prices):
            # first we check to see if right < left
            # meaning it would have been better to buy on this day than the one we had picked previously
            # if that is the case, we setup a new left and right pointer around this date
            if prices[right] < prices[left]:
                left = right
                right = left + 1
                continue

            # otherwise we check the possible profit to see if it beats the best scenario found so far
            profit = prices[right] - prices[left]
            # print(f"checking {left} and {right} with a possible profit of {profit}")
            if profit > best_profit:
                best_buy = left
                best_sell = right
                best_profit = profit

            # and we continue scanning to make sure we have the best possible profit
            if right < len(prices):
                right = right + 1

        return best_profit

        # space complexity O(1), just a few pointers uses.
        # time complexity O(N) to scan the list of numbers once through.






