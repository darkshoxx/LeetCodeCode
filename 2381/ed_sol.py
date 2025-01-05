# Approach 1

from typing import List


class Solution1:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_register = [0]*len(s)
        for sequence in shifts:
            if sequence[2]==1:
                offset = 1
            else:
                offset = -1
            prefix_register[sequence[0]] += offset
            if sequence[1]+1 < len(s):
                prefix_register[sequence[1]+1] -= offset
        shift_register = [prefix_register[0]]
        for index in range(1, len(s)):
            shift_register.append(shift_register[index-1]+ prefix_register[index])
        letters = [chr((ord(letter) + offset - ord('a'))%26 + ord("a"))
                   for letter, offset in zip(s,shift_register)
                   ]
        return "".join(letters)
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.shiftingLetters
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)