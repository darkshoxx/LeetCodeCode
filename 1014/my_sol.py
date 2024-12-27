from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left_optimal = [values[i] + i for i in range(len(values))]
        right_optimal = [values[i] - i for i in range(len(values))]
        current_max = -1
        for i in range(len(values)-1):
            for j in range(i+1, len(values)):
                my_sum = left_optimal[i] + right_optimal[j]
                if my_sum > current_max:
                    current_max = my_sum
        return current_max
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.maxScoreSightseeingPair
    checks = [solve_method(*[input]) == output for input, output in zip(inputs, outputs)]
    print(checks)