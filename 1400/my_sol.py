from typing import List


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        letters = [0]*26
        for letter in s:
            letters[ord(letter) - ord("a")] +=1
        numbers = 0
        odds = 0
        for letter in letters:
            if ((letter % 2) != 0):
                odds +=1
            numbers += letter
        if k <= numbers:
            if odds <= k:
                return True
        return False

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.canConstruct
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)