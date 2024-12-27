# Approach 1

from typing import List


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_ways = 0
        self.calculate_ways(nums, current_index = 0, current_sum = 0, target=target)
        return self.total_ways
    
    def calculate_ways(self, nums: List[int], current_index: int, current_sum: int, target: int):
        if current_index == len(nums):
            if current_sum == target:
                self.total_ways += 1
        else:
            self.calculate_ways(nums, current_index+1, current_sum + nums[current_index], target)
            self.calculate_ways(nums, current_index+1, current_sum - nums[current_index], target)

# Approach 2
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_sum = sum(nums)
        init_row = [None]*(2*self.total_sum+1)
        memo = [init_row[:] for _ in range(len(nums))]
        value = self.calculate_ways(nums, current_index = 0, current_sum = 0, target=target, memo=memo)
        return value
    
    def calculate_ways(self, nums: List[int], current_index: int, current_sum: int, target: int, memo:List):
        if current_index == len(nums):
            if current_sum == target:
                return 1
            return 0
        entry = memo[current_index][current_sum+self.total_sum]
        if entry is not None:
            return entry
        add = self.calculate_ways(nums, current_index+1, current_sum + nums[current_index], target, memo)
        subtract = self.calculate_ways(nums, current_index+1, current_sum - nums[current_index], target, memo)
        memo[current_index][current_sum+self.total_sum] = add + subtract
        return add + subtract
# Approach 3
class Solution3():
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_sum = sum(nums)
        init_row = [0]*(2*self.total_sum+1)
        dp = [init_row[:] for _ in range(len(nums))]
        dp[0][nums[0] + self.total_sum]+=1 
        dp[0][-nums[0] + self.total_sum]+=1 
        for index in range(1,len(nums)):
            for possible_sum in range(-self.total_sum, self.total_sum+1):
                if dp[index-1][possible_sum+self.total_sum]>0:
                    dp[index][possible_sum +nums[index] + self.total_sum] += dp[index-1][possible_sum+self.total_sum]
                    dp[index][possible_sum -nums[index] + self.total_sum] += dp[index-1][possible_sum+self.total_sum]
        if abs(target) > self.total_sum:
            return 0
        return dp[len(nums)-1][target + self.total_sum]

# Approach 4
class Solution4():
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0]*(2*total_sum+1)
        dp[nums[0]+total_sum] = 1
        dp[-nums[0]+total_sum] += 1
        for index in range(1,len(nums)):
            next_row = [0]*(2*total_sum+1)
            for possible_sum in range(-total_sum, total_sum+1):
                if dp[possible_sum + total_sum]>0:
                    next_row[possible_sum +nums[index] + total_sum] += dp[possible_sum+total_sum]
                    next_row[possible_sum -nums[index] + total_sum] += dp[possible_sum+total_sum]
            dp = next_row
        if abs(target) > total_sum:
            return 0
        return dp[target + total_sum]
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution2()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution3()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution4()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)