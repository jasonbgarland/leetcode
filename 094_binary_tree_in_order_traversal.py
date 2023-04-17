"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recursive_solution(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution
        # in order traversal of a binary tree means visiting the left child, then root,
        # then right child for every node in the tree
        def traverse(node: Optional[TreeNode]):
            if node:
                # process left node
                traverse(node.left)

                # add output of root node (this node's value)
                output.append(node.val)

                # process right node
                traverse(node.right)

        output = []
        traverse(root)

        return output

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution
        # use a stack to remember what nodes still need further processing
        # this is kind of silly but I guess it's a check to see if you can simulate the way
        # the recursion might be working behind the scenes

        output = []
        stack = []
        current = root

        # while there is still something to do, meaning there are things on the stack or the current node isn't None
        while current or stack:

            # keep traversing left
            while current:
                stack.append(current)
                current = current.left

            # done with left most, so we can go back up one, add the value, and then process the right node
            current = stack.pop()
            output.append(current.val)
            # and now process the right side
            current = current.right

        return output


