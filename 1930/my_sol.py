from typing import List


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_to_seconds = {}
        # dict key: letter value: set of second letters to form palindrome
        letter_set = set()
        for letter in s:
            letter_set.add(letter)
        num_letters = len(letter_set)
        front_index = 0
        back_index = len(s)-1
        while front_index != len(s) - 2:
            if s[front_index] not in first_to_seconds.keys():
                current_letter = s[front_index]
                while s[back_index] != current_letter and back_index != front_index:
                    back_index -= 1
                if back_index == front_index:
                    back_index = 0
                else:
                    current_letter_set = set()
                    middle_index = front_index + 1
                    while middle_index != back_index and len(current_letter_set) != num_letters:
                        current_letter_set.add(s[middle_index])
                        middle_index += 1
                    # for middle_index in range(front_index + 1, back_index): # change to while if too slow, skip after 26                
                    #     current_letter_set.add(s[middle_index])
                    first_to_seconds[current_letter] = current_letter_set
            front_index += 1
            back_index = len(s)-1
        accumulator = 0
        for value in first_to_seconds.values():
            accumulator += len(value)
        return accumulator

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countPalindromicSubsequence
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)