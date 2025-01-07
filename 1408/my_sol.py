from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        from itertools import combinations
        my_set = set()
        for a,b in combinations(words, 2):
            
            if a in b:
                my_set.add(a)
            if b in a:
                my_set.add(b)
        return list(my_set)

    

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.stringMatching
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)