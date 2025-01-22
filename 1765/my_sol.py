from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        pass

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.highestPeak
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)