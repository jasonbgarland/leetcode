"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def firstPass(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # this solution doesn't submit because it runs out of memory. It's of course not very efficient!
        # the requirements stating that a solution can be found in O(m + n) makes me think that the worst case scenario is scanning both lists
        # we'll have two pointers, left and right
        # left will be the index pointer
        # we look at nodes along the right list, and keep going until the end of the list
        left = headA

        while left:
            right = headB
            while right:
                # print(f"left is {left.val} right is {right.val}")
                if left == right:
                    return left
                right = right.next

            left = left.next

        return None

    def highMemorySolution(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # this one also times out because it is inneficient

        # in this solution we keep track of all the nodes we see while we visit A
        # then traverrse B until we see one that is in common
        left = headA
        right = headB
        visited = set()

        while left:
            visited.add(left)
            left = left.next

        while right:
            if right in visited:
                return right

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # had to look this one up
        # it's a bit of a trick solution
        # if you think about it, once the lists intersect, they will have the same length / number of nodes until the end
        # so if you know the lengths of both lists, you can "even them out" (move the longer list forward) until they have the same number of nodes left
        # once that is the case, you increment both lists until they are pointing to the same node

        left = headA
        right = headB

        length_a = 0
        while left:
            length_a = length_a + 1
            left = left.next

        length_b = 0
        while right:
            length_b = length_b + 1
            right = right.next

        print(f"length a is {length_a} length b is {length_b}")

        # we don't know which one is larger, so we have to account for either condition
        if length_a > length_b:
            longer = headA
            shorter = headB
            difference = length_a - length_b
        else:
            longer = headB
            shorter = headA
            difference = length_b - length_a

        # now we move the longer list forward the amount of times of the difference
        index = 0
        while index < difference:
            index = index + 1
            longer = longer.next

        print(f"longer is starting at value {longer.val}")

        # now both lists are an even length until the end, so we just keep checking until they have crossed
        while shorter != longer:
            print(f"comparing nodes with value {shorter.val} and {longer.val}")
            shorter = shorter.next
            longer = longer.next

        # they are crossing, so return either of the references
        return shorter

        # time complexity is O(m + n + the number of nodes until they intersect, which could be m or n whichever is larger) = O(m + n) = O(n)
        # space complexity is O(1) since the size of the used memory does not change based on the size of the inputs


