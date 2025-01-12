# Approach 1

from typing import List


class Solution1:
    def canConstruct(self, s: str, k: int) -> bool:
        pass
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.canConstruct
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)