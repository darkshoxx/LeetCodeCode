from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        my_len = len(pref)
        accumulator = 0
        for word in words:
            if len(word) >= my_len:
                if word[:my_len] == pref:
                    accumulator += 1
        return accumulator

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.prefixCount
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)