from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        candidate_1, candidate_2 = edges[0]
        if candidate_1 in edges[1]:
            return candidate_1
        return candidate_2

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)