"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # since we have at least one element, we know there is at
        # least one unique element. It goes into slot 0 (which is 1-1)
        unique = 1

        # we will start at the next element
        index = 1

        # as long as there are more elements to look at
        while index <= len(nums)-1:
            print(f"unique: {unique, nums[unique-1]}, index={index, nums[index]}")
            # if the element is different than the last unique one
            # we increment unique, and put the new number at the unique-1 slot
            if nums[unique-1] != nums[index]:
                nums[unique] = nums[index]
                unique +=1

            # each iteration we move our index pointer one more forward
            # continuing until we have looked at each element
            index +=1

        # since we've kept track of unique elements
        # (and used them to know where to place them in the final array)
        # we can just return that counter as the result
        return unique
