from typing import List

# Doesn't work
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        freq_dict = {}
        for entry in nums:
            if entry in freq_dict:
                freq_dict[entry] += 1
            else:
                freq_dict[entry] = 1
        sorted_list = sorted(freq_dict.keys())

        index = 0
        jndex = len(sorted_list) - 1
        all_pairs_found = False
        val_i = sorted_list[index]
        val_j = sorted_list[jndex]
        anchor_i = None
        anchor_j = None
        fair_pairs = 0
        while not all_pairs_found:
            if val_i + val_j > upper:
                jndex -= 1
                if jndex < index:
                    all_pairs_found = True
                else:
                    val_j = sorted_list[jndex]
            else:
                anchor_j = jndex
            if lower > val_i + val_j:
                index += 1
                if jndex < index: 
                    all_pairs_found = True
                else:
                    val_i = sorted_list[index] 
            else:
                anchor_i = index
            if anchor_i is not None and anchor_j is not None:
                while anchor_i <= anchor_j:
                    for runner in range(anchor_i, anchor_j+1):
                        if lower <= sorted_list[runner] + sorted_list[anchor_j]<= upper:
                            if runner == anchor_j:
                                fair_pairs += int(freq_dict[sorted_list[runner]]*(freq_dict[sorted_list[anchor_j]]-1)/2)
                            else:
                                fair_pairs += freq_dict[sorted_list[runner]]*freq_dict[sorted_list[anchor_j]]
                    anchor_j -= 1
                    if sorted_list[anchor_i] + sorted_list[anchor_j] > upper:
                        anchor_i +=1
                all_pairs_found = True
        return fair_pairs
                

# too slow
class Solution1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        freq_dict = {}
        for entry in nums:
            if entry in freq_dict:
                freq_dict[entry] += 1
            else:
                freq_dict[entry] = 1

        fair_pairs = 0
        for index in freq_dict:
            for jndex in freq_dict:
                if jndex < index:
                    if lower <= index + jndex <= upper:
                        fair_pairs += freq_dict[index]*freq_dict[jndex]
                if jndex == index:
                    if lower <= index + jndex <= upper:
                        fair_pairs += int(freq_dict[index]*(freq_dict[index]-1)/2)
        return fair_pairs

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countFairPairs
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)