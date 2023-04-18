"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []

        # two pointers, one for each string
        left = 0
        right = 0
        while left < len(word1) or right < len(word2):
            # process left
            if left < len(word1):
                output.append(word1[left])
                left = left + 1
            elif right < len(word2):
                # if nothing left for word1, take a char from word2
                output.append(word2[right])
                right = right + 1

            # process right
            if right < len(word2):
                output.append(word2[right])
                right = right + 1
            elif left < len(word1):
                # if nothing left for word2, take a char from word1
                output.append(word1[left])
                left = left + 1

        # assemble the string from the list
        return "".join(output)

