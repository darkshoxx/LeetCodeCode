# Approach 1

from typing import List


class Solution1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            low = self.lower_bound(nums, i+1, len(nums)-1, lower - nums[i])
            high = self.lower_bound(nums, i+1, len(nums)-1, upper - nums[i] + 1)
            ans += high-low
        return ans

    def lower_bound(self, nums, low, high, element):
        while low <= high:
            mid = low + int((high-low)/2)
            if nums[mid]>= element:
                high = mid - 1
            else:
                low = mid + 1
        return low
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.countFairPairs
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)