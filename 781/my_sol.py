from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_dict = {}
        for answer in answers:
            if answer not in freq_dict:
                freq_dict[answer] = 1
            else:
                freq_dict[answer] += 1
        accumulator = 0
        for reply, frequency in freq_dict.items():
            multiples = frequency // (reply+1)
            remainder = frequency % (reply+1)
            if remainder == 0:
                accumulator += frequency
            else:
                accumulator += (reply+1)(multiples+1)
        return accumulator




if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.numRabbits
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)