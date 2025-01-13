from typing import List


class Solution:
    def minimumLength(self, s: str) -> int:
        my_dict = {}
        for letter in s:
            if letter in my_dict:
                my_dict[letter] ^= True
            else:
                my_dict[letter] = True
        accumulator = 0
        for value in my_dict.values():
            if value:
                accumulator += 1
            else:
                accumulator += 2
        return accumulator


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.minimumLength
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)