"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import queue


class Solution:
    def first_pass(self, stones: List[int]) -> int:
        # The easiest way, not the most efficient way

        # sort the numbers
        working_list = sorted(stones)

        # keep playing until 0 or 1 stones remaining
        while len(working_list) > 1:
            # take the two largest
            # the end element should be >= the 2nd from the end
            y, x = working_list.pop(), working_list.pop()
            if x == y:
                # both stones have been removed
                continue
            else:
                # adjust the size of the remaining stone and re insert it
                working_list.append(y - x)
                # resort the list
                working_list.sort()

        # edge case where there are no stones left. Return 0
        if len(working_list) == 0:
            return 0

        # return the weight of the remaining stone
        return working_list[0]

    def lastStoneWeight(self, stones: List[int]) -> int:
        # try using a heap or priority queue to store and retrieve the data
        # this is because all we care about at any moment is retrieving largest element

        # Python has a built in heap - heapq. It keeps track of the smallest element
        # Because of this we will have to negate each value in the list before setting up the heap

        # the time complexity for both push and pop for heapq is O(log(n))
        # it involves adding the element and then shifting targetted elements until the heap invariant is true
        stone_heap = [-x for x in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            # take the two largest

            # the end element should be >= the 2nd from the end
            y, x = heapq.heappop(stone_heap) * -1, heapq.heappop(stone_heap) * -1
            print(f"y is {y} and x is {x}")
            if x == y:
                # both stones have been removed
                continue
            else:
                heapq.heappush(stone_heap, (y - x) * -1)

        # edge case where there are no stones left. Return 0
        if len(stone_heap) == 0:
            return 0

        # return the weight of the remaining stone
        return heapq.heappop(stone_heap) * -1


