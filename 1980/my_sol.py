from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        pass

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findDifferentBinaryString
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)