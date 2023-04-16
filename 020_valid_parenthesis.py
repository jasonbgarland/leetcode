"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        for element in s:
            # print(f"element is {element} and x is {x}")
            if element in ["(", "{", "["]:
                x.append(element)
                continue

            # if there is nothing to pull from, string is unbalanced
            if not x:
                return False

            prev = x.pop()
            # print(f"prev is {prev} and element is {element}")
            if prev == "(" and element == ")":
                continue
            if prev == "{" and element == "}":
                continue
            if prev == "[" and element == "]":
                continue

            # all other cases are invalid
            return False

        # if there are any leftover brackets, they are not balanced
        if x:
            return False

        # string is balanced
        return True



