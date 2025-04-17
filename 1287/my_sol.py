from typing import List

import math
# works and is faster
class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        threshold = math.floor(len(arr)/4)
        counter = 1
        lagged_value = arr[0]
        for entry in arr[1:]:
            if entry == lagged_value:
                counter +=1
            else:
                counter = 1
            lagged_value = entry
            if counter > threshold:
                return entry


# works but bad
class Solution1:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = math.floor(len(arr)/4)
        occurrence_dict = {}
        for entry in arr:
            if entry in occurrence_dict:
                occurrence_dict[entry] +=1
            else:
                occurrence_dict[entry] = 1
            if occurrence_dict[entry]>threshold:
                return entry

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findSpecialInteger
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)