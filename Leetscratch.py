from typing import List


class Solution:
    lookup = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if tuple(nums) in self.lookup.keys():
            return self.lookup[tuple(nums)]
        if len(nums) == 1:
            my_sum = 0
            if nums[0] == target:
                my_sum +=1
            if nums[0] == -target:
                my_sum +=1
            self.lookup[tuple(nums)] = my_sum
            return my_sum
        num_copy = nums[:]
        item = num_copy.pop()
        ret_val = self.findTargetSumWays(num_copy, target - item) + self.findTargetSumWays(num_copy, target + item)
        self.lookup[tuple(nums)] = ret_val
        return ret_val
        # accumulator = 0
        # my_length = len(nums)
        # for i in range(2**my_length):
        #     bin_string = format(i, f'0{my_length}b')
        #     signs = [1  if bina == "1" else -1 for bina in bin_string]
        #     if target == sum(num*sign for num, sign in zip(nums, signs)):
        #         accumulator +=1
        # return accumulator



a = Solution()
result = a.findTargetSumWays([1,1,1,1,1], 1)
print(result)
