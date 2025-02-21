from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        count = Counter(tiles)
        frequency = list(count.values())
        result =  self.choose_one(frequency)
        print(result)
        return result
        
    def choose_one(self, frequency:List):
        if len(frequency)==0:
            return 0
        sub_count = 0
        for i in range(len(frequency)):
            sub_frequency = frequency[:]
            if sub_frequency[i] == 1:
                sub_frequency.pop(i)
            else:
                 sub_frequency[i] -= 1
            sub_count += self.choose_one(sub_frequency) +1 #+1 for strings ending here.
        return sub_count 




if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.numTilePossibilities
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)