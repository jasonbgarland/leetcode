"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # can use two pointers
        # and a binary search to keep reducing the solution
        # set in half until we find the best fit
        left = 0
        right = x
        possible_result = 0

        while left <= right:
            midpoint = (left + right) // 2
            print(f"midpoint: {midpoint}, square: {midpoint ** 2}")

            if midpoint ** 2 > x:
                # chop search space in half
                # look to the left side
                right = midpoint - 1
            elif midpoint ** 2 < x:
                # search to the right next
                left = midpoint + 1
                # store this number, as it might be the closest we have
                # because one int higher might be too high
                possible_result = midpoint
            else:
                # if we found the value, then return it
                return midpoint

        return possible_result
