from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        results = []
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                results.append(i)
        return results

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.stableMountains
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)