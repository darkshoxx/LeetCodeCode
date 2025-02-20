from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = [str(1-int(nums[i][i])) for i in range(len(nums))]
        return "".join(result)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findDifferentBinaryString
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)