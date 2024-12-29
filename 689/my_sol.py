from typing import List
from itertools import combinations

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        from itertools import accumulate
        prefix = [0] + list(accumulate(nums))
        left_best_index = [0]*n
        right_best_index = [0]*n
        current_max_sum = prefix[k]- prefix[0]
        for i in range(k, n):
            current_sum = prefix[i+1] - prefix[i+1-k]
            if current_sum > current_max_sum:
                current_max_sum = current_sum
                left_best_index[i] = i + 1 - k
            else:
                left_best_index[i] = left_best_index[i-1]

        right_best_index[n-k] = n-k
        current_max_sum = prefix[n]- prefix[n-k]

        for i in range(n-k-1, -1, -1):
            current_sum = prefix[i + k] - prefix[i]
            if current_sum >= current_max_sum:
                current_max_sum = current_sum
                right_best_index[i] = i
            else:
                right_best_index[i] = right_best_index[i+1]
        current_max_sum = 0
        for middle_index in range(k, n-2*k+1):
            left = left_best_index[middle_index - 1]
            right = right_best_index[middle_index + k]
            current_sum = (
                -prefix[left] + prefix[left +k] +
                -prefix[middle_index] + prefix[middle_index +k]+
                -prefix[right] + prefix[right +k] 
            )
            if current_sum > current_max_sum:
                current_max_sum = current_sum
                triplet = [left, middle_index, right]
        return triplet

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.maxSumOfThreeSubarrays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)