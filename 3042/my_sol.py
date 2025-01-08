from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        from itertools import combinations
        accumulator = 0
        for left, right in combinations(words, 2):
            if self.is_prefix_and_suffix(left, right):
                accumulator +=1
        return accumulator
    def is_prefix_and_suffix(self, str1, str2):
        len_1 = len(str1)
        len_2 = len(str2)
        if len_1 > len_2:
            return False
        for i in range(len_1):
            if str1[i] != str2[i]:
                return False
            if str1[i] != str2[len_2 - len_1 + i]:
                return False
        return True

            

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countPrefixSuffixPairs
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)