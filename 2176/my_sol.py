from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        accumulator = 0
        index_dict = {}
        for index, value in enumerate(nums):
            if value not in index_dict:
                index_dict[value] = [index]
            else:
                for position in index_dict[value]:
                    if (position*index % k == 0):
                        accumulator += 1
                index_dict[value].append(index)
        return accumulator


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countPairs
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)