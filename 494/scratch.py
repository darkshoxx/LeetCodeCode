from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        # Initialize the first row of the DP table
        dp[nums[0] + total_sum] = 1  # Adding nums[0]
        dp[-nums[0] + total_sum] += 1  # Subtracting nums[0]

        # Fill the DP table
        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp

        # Return the result if the target is within the valid range
        return 0 if abs(target) > total_sum else dp[target + total_sum]        
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)