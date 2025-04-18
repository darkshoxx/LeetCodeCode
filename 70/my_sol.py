from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        value_1 = 1
        value_2 = 1
        mid_sum = 1
        for _ in range(n-1):
            mid_sum = value_2 + value_1
            value_2 = value_1
            value_1 = mid_sum
        return mid_sum
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.climbStairs
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)