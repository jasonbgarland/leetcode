"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    def firstPass(self, nums: List[int]) -> int:
        # this solution works and is fast, but uses more space
        # store the counts of each number as we go through the list
        # if we've hit a new high, keep track of that as we go
        value = 0
        highest = 0
        counts = {}
        for num in nums:
            print(f"max is {max} value is {value} and counts is {counts}")
            counts[num] = counts.get(num, 0) + 1
            highest = max(counts[num], highest)
            if counts[num] == highest:
                value = num

        return value

    def majorityElement(self, nums: List[int]) -> int:
        # booyer moore algorithm (another trick, I'm shocked.....)

        # start with result as the first element, and the count of that element is 1
        # keep going to the right, if the number matches, add a counter
        # if it doesn't match, decrement the counter
        # each time the counter reaches 0, replace the result with that number, reset the count to 1
        # this works because the numbers will even out until you find the one that is in the array more times than the rest

        result = 0
        count = 0

        for num in nums:
            print(f"result is {result} and count is {count}")
            if count == 0:
                result = num

            # if the number matches, increment, if it doesn,t decrement
            count = count + (1 if num == result else -1)

        return result
