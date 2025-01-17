from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not (derived.count(1) % 2)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.doesValidArrayExist
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)