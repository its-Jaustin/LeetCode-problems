# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n==1:
            return 1
        elif n == 2:
            return 2
        arr = {}
        arr[0] = 1
        arr[1] = 2
        for x in range(2, n):
            arr[x] = arr[x-2] + arr[x-1]
        return arr[n-1]