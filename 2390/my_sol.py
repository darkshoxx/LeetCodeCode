from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for entry in s:
            if entry != "*":
                stack.append(entry)
            else:
                stack.pop()
        return "".join(stack)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)