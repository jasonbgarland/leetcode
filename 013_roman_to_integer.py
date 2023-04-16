"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        special_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        total = 0

        working = list(s)
        while len(working) > 0:
            print(f"total: {total}")
            current_character = working.pop(0)
            print(f"current character: {current_character}")
            if len(working) > 0:
                next_character = working[0]
                print(f"next character: {next_character}")
                if current_character + next_character in special_cases.keys():
                    total = total + special_cases[current_character + next_character]
                    print(f"new total: {total}\n")
                    # don't forget to remove the next character from the string too!
                    working.pop(0)
                    continue
            total = total + conversions[current_character]
            print(f"new total: {total}\n")
        return total







