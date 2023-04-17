"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:

    def brute_force(self, s: str) -> int:
        # first attempt: brute force method: O(n^2)
        # two pointers, a candiate pointer and a checker pointer that checks to see if there are any repeats
        # the pointers point to the index of the string where the character is

        candidate = 0
        disqualified_candidates = []

        while candidate < len(s):
            if s[candidate] in disqualified_candidates:
                candidate = candidate + 1
                continue

            checker = candidate + 1
            print(f"checking for any more occurences of candidate {s[candidate]}")
            while checker < len(s) and (s[candidate] != s[checker]):
                checker = checker + 1

            # check to see if we found it
            if checker == len(s):
                return candidate
            else:
                print(f"{s[candidate]} is not unique in the string")
                disqualified_candidates.append(s[candidate])
                candidate = candidate + 1

        # we went through the whole string and didn't find any unique characters, so return -1
        return -1

    def firstUniqChar(self, s: str) -> int:
        # second attempt, less iterations through the string
        # we do one pass, keeping track of the counts of each character
        # and then one more pass, comparing each character to the counts
        # the first one we get to that has a count of one, we know the index
        # this gives us a time complexity of O(n) plus up to n to compare the counts with the first occurence
        # which is O(n + n) = O(n)

        # note: here we could use collections.Counter to do the counting for us, but not sure if that is "cheating" or not
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for index, char in enumerate(s):
            if counts.get(char, 0) == 1:
                return index

        # no characters that only occur once, so return -1
        return -1



