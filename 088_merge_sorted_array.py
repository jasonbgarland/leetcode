"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # edge case where m = 0
        if m == 0:
            print("no elements in nums1, so fill in with contents of nums2")
            for index, element in enumerate(nums2):
                nums1[index] = element
            return
        # edge case where n = 0
        if n == 0:
            print("no elements in nums2, so nums1 is correct")
            # nothing to do, as nums1 is already in the correct final state
            return

        # we will fill in the array from right to left, taking the higher of each number between left and right
        # until we run out of numbers / slots to fill

        # left points at the end of the nums1 set (this might not be the end of the index because of the 0 padding)
        left = m-1

        # right points at the end of the nums2 set
        right = n-1

        # and a third number to point at the end of the array
        tail = m+n-1
        while tail >= 0:
            print(f"tail is {tail}, left is {left} and right is {right}")
            if right < 0:
                nums1[tail] = nums1[left]
                left = left - 1
            elif left < 0:
                nums1[tail] = nums2[right]
                right = right -1
            elif nums1[left] >= nums2[right]:
                nums1[tail] = nums1[left]
                left = left - 1
            else:
                nums1[tail] = nums2[right]
                right = right -1

            tail = tail - 1
            print(f"nums1 is now {nums1}")




