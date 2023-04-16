"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case for needle empty
        if needle == "":
            return -1

        # edge case for if needle bigger than haystack
        if len(needle) > len(haystack):
            return -1

        # scan until you find the first character
        # mark the position

        start_index = 0
        while start_index < len(haystack):
            if haystack[start_index] != needle[0]:
                start_index += 1
                continue

            print(f"possible start index is {start_index}")

            verified = 0
            for index, element in enumerate(needle):
                if start_index + index >= len(haystack):
                    return -1

                print(f"checking {haystack[start_index + index]} == {needle[index]}")
                if haystack[start_index + index] == needle[index]:
                    verified += 1
                else:
                    break
            if verified == len(needle):
                return start_index

            start_index += 1

        return -1

        #