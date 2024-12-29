from typing import List


class Solution:
    from functools import cache
    def numWays(self, words: List[str], target: str) -> int:
        # register dict: keys: letters of target, values: dict
        #    keys:letter index, value: number of words that contain target letter at that index
        self.word_length = len(words[0])
        self.target = target
        self.register = {}
        for letter in target:
            if letter not in self.register.keys():
                inter_dict = {index:0 for index in range(len(words[0]))}
                for word in words:
                    for i in range(len(word)):
                        if word[i] == letter:
                            inter_dict[i] += 1
                self.register[letter] = inter_dict
        accumulator = 0
        for start_index in range(self.word_length - len(self.target)+1):
            accumulator += self.possibilities(0, start_index)
        return accumulator
    
    @cache
    def possibilities(self, target_index, letter_index):
        if target_index == len(self.target) - 1:
            return self.register[self.target[target_index]][letter_index]
        if letter_index > self.word_length:
            return 0
        accumulator = 0
        for next_index in range(letter_index + 1, self.word_length - (len(self.target) - target_index-1)+1):
            accumulator += self.possibilities(target_index + 1, next_index)
        return accumulator * self.register[self.target[target_index]][letter_index]




if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.numWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)