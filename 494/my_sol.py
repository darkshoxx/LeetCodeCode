


from typing import List

# Recursion with Memoization
class Solution:
    lookup = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        compare_tuple = tuple(nums[i] if i<len(nums) else target for i in range(len(nums)+1))
        if compare_tuple in self.lookup.keys():
            return self.lookup[compare_tuple]
        if len(nums) == 1:
            my_sum = 0
            if nums[0] == target:
                my_sum +=1
            if nums[0] == -target:
                my_sum +=1
            self.lookup[compare_tuple] = my_sum
            return my_sum
        num_copy = nums[:]
        item = num_copy.pop()
        ret_val = self.findTargetSumWays(num_copy, target - item) + self.findTargetSumWays(num_copy, target + item)
        self.lookup[compare_tuple] = ret_val
        return ret_val


a = Solution()
result = a.findTargetSumWays([1,1,1], 1)
# print(result)


##  previous solution, timeout
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#     accumulator = 0
#     my_length = len(nums)
#     for i in range(2**my_length):
#         bin_string = format(i, f'0{my_length}b')
#         signs = [1  if bina == "1" else -1 for bina in bin_string]
#         if target == sum(num*sign for num, sign in zip(nums, signs)):
#             accumulator +=1
#     return accumulator
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)