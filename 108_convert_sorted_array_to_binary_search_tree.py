"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # start with two pointers at both ends
        left = 0
        right = len(nums) - 1

        def create_subtree(left: int, right: int):
            print(f"create called with left: {left} and right {right}")
            # if there is only one element left, it is the root
            if left == right:
                return TreeNode(val=nums[left])

            if right < left:
                return None

            midpoint = (left + right) // 2
            node = TreeNode()
            node.val = nums[midpoint]
            node.left = create_subtree(left, midpoint - 1)
            node.right = create_subtree(midpoint + 1, right)
            return node

        result = create_subtree(left, right)
        return result
