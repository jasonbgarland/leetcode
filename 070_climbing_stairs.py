"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # the hard part here is keeping track of all the permutations
        # we can think of the solution as a series of steps, deciding first if we take one or two steps
        # and then looking at the number of solutions that branch off of each step.
        # in the end we total all the steps

        # along the way you realize that there are a lot of repeat calculations, so if you remember the answers
        # to the calculations, the processing speeds up over time

        # we will creating a mapping that stores the number of possible permutations if the step you just took results in N steps left to go
        # so if you went from 1 step to go, to zero steps to go, there was one solution (you are done basically)
        # if you went from 2 steps down to 1 step to go, there is also one solution (take the last step!)
        subs = {0: 1, 1: 1}

        def calculate_remaining(x: int):
            # if we already know the answer, return it
            possible_solution = subs.get(x, None)
            if possible_solution:
                return possible_solution

            # if we don't know the answer
            # calculate solutions from each decision
            solution = calculate_remaining(x - 1) + calculate_remaining(x - 2)
            # store solution
            subs[x] = solution
            return solution

        return calculate_remaining(n)

