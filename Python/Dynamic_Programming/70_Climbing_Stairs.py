class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev_2 = 2
        prev_1 = 3
        for i in range(3, n):
            temp = prev_1
            prev_1 += prev_2
            prev_2 = temp
        return prev_1
