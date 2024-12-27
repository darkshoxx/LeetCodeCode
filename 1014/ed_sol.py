from typing import List

# Approach 1
class Solution1:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left_score = [-1]*len(values)
        max_left_score[0] = values[0]
        max_score = 0
        for i in range(1, len(values)):
            current_right = values[i] - i
            max_score = max(max_score, max_left_score[i-1] + current_right)
            current_left = values[i] + i
            max_left_score[i] = max(max_left_score[i-1], current_left)
        return max_score

# Approach 2
class Solution2:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left_score = values[0]
        max_score = 0
        for i in range(1, len(values)):
            current_right = values[i] - i
            max_score = max(max_score, max_left_score + current_right)
            current_left = values[i] + i
            max_left_score = max(max_left_score, current_left)
        return max_score
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.maxScoreSightseeingPair
    checks = [solve_method(*[input]) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution2()
    solve_method = solution_object.maxScoreSightseeingPair
    checks = [solve_method(*[input]) == output for input, output in zip(inputs, outputs)]
    print(checks)