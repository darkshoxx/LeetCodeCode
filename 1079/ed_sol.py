# Approach 1

from typing import List


class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        pass
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.numTilePossibilities
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)