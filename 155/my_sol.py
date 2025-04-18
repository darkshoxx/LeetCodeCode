from typing import List

# cannot be run, as not compatible with test environment. But works
# Alternative soltuion replaces
#     def __init__(self):
#         self.stack = []
# with
#     def __init__(self):
#         self.stack = deque()
# and 
# from collections import deque
# at the top
class MinStack:

    def __init__(self):
        self.stack = []
        self.popped = False
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is not None:
            self.min = min(self.min, val)
        else:
            self.min = val        

    def pop(self) -> None:
        self.stack.pop()
        self.popped = True
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.popped:
            return min(self.stack)
        else:
            return self.min
        

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pass

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)