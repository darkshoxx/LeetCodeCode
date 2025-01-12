from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        global_frequency = [0]*26
        local_frequency = [0]*26
        for word in words2:
            for letter in word:
                letter_index = ord(letter) - ord("a")
                local_frequency[letter_index] += 1
            for index in range(26):
                global_frequency[index] = max(global_frequency[index], local_frequency[index])
            local_frequency = [0]*26
        return_list = []
        for word in words1:
            for letter in word:
                letter_index = ord(letter) - ord("a")
                local_frequency[letter_index] += 1
            valid = True
            for index in range(26):
                if valid and local_frequency[index] < global_frequency[index]:
                    valid = False
            if valid:
                return_list.append(word)
            local_frequency = [0]*26
        return return_list
        

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.wordSubsets
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)