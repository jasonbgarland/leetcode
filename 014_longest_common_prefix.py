"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def common_str(self, strs: List[str], index: int):
        chars = set()

        for thing in strs:
            try:
                chars.add(thing[index])
            except IndexError:
                return ""
        if len(chars) == 1:
            return list(chars)[0]
        return ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        for index in range(len(strs[0])):
            print(f"longest_prefix: {longest_prefix} | current_index: {index}")
            additional_char_for_prefix = self.common_str(strs, index)
            print(f"additional_char: {additional_char_for_prefix}")

            if additional_char_for_prefix == "":
                return longest_prefix
            longest_prefix = longest_prefix + additional_char_for_prefix

        return longest_prefix
