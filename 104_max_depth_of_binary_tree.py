"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def first_pass(self, root: Optional[TreeNode]) -> int:
        # this solution is clear, but there was a suspicion I could have cleaned it up some.

        # this is like a traverse and print problem, but instead of printing we are keeping track of the number of nodes visited in each sub stree
        # if the node is None, it adds a 0 value to the counter
        # otherwise it calculates all the values below it +
        if root is None:
            return 0

        def count_nodes(left: Optional[TreeNode], right: Optional[TreeNode]) -> int:
            # process left
            if left is None:
                left_count = 0
            else:
                left_count = 1 + count_nodes(left.left, left.right)

            # process right
            if right is None:
                right_count = 0
            else:
                right_count = 1 + count_nodes(right.left, right.right)

            # return the larger number
            if left_count >= right_count:
                return left_count
            return right_count

        # our total nodes is 1 (for the root node level) plus the total of the largest path below it
        return 1 + count_nodes(root.left, root.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # The is the same logic as the first_pass I wrote, but after watching youtube I discovered there WAS a cleaner way, and this is it

        def count(node: Optional[TreeNode]) -> int:
            # if this is not a node (is None) then it shouldn't count towards the total depth
            if node is None:
                return 0

            # otherwise there is a left or right side, so we run the calculation recursively on both children and take the larger result
            # making sure to add one to the total, which represents the count for the current depth
            return 1 + max(count(node.left), count(node.right))

        return count(root)