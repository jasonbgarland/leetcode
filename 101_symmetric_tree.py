"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(left, right):
            # check the nodes at a certain level

            # Check if both nodes are empty
            if left is None and right is None:
                return True

            # if only one node has data, can return False early
            if left is None or right is None:
                return False

            # check center value
            center_ok = left.val == right.val

            # now check the children, which is where we get into the recursive part
            # check that left side of the left node is the same as the right side of the right node
            left_side_ok = check(left.left, right.right)
            right_side_ok = check(left.right, right.left)

            # note: we can save some processing by also putting it all inf a long if statement, but it is less readable:
            # return (left.val == right.val) and check(left.left, right.right) and check(left.right, right.left)

            if center_ok and left_side_ok and right_side_ok:
                return True
            return False

        return check(root.left, root.right)

