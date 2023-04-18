"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        if numRows == 1:
            return result

        def generate_row(previous_row: List):
            print(f"previous row: {previous_row}")
            output = []
            for index in range(len(previous_row) + 1):
                print(f"calculating element {index}")
                if index == 0 or index == len(previous_row):
                    output.append(1)
                else:
                    output.append(previous_row[index - 1] + previous_row[index])
            print(f"generated row is {output}")
            return output

        for x in range(numRows - 1):
            print(f"generating row {x}")
            result.append(generate_row(result[-1]))
            print(f"result is now {result}")
        return result

# time complexity is O(n^2) since we used two loops
# space complexity is 1 + 2 + 3 + 4 + 5 etc for n rows
# not sure how to express that
# googling says it is O(n^2) as well


