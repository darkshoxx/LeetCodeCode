from typing import List

#TOO SLOW
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        levels = len(possible)
        positives = sum(possible)
        negatives = levels-positives
        total_score = positives - negatives
        alice = 0
        bob = total_score
        for index in range(len(possible)-1):
            if possible[index]:
                alice += 1
                bob -= 1
            else:
                alice -= 1
                bob += 1
            if alice > bob:
                return index + 1
        return -1

#TOO SLOW
class Solution1:
    def minimumLevels(self, possible: List[int]) -> int:
        current_score = 0
        for index, value in enumerate(possible[:len(possible)-1]):
            if value:
                current_score +=1
            else:
                current_score -=1
            lookahead = 0
            for item in possible[(index+1):]:
                if item:
                    lookahead +=1
                else:
                    lookahead -=1
            if current_score > lookahead:
                return index + 1
        return -1

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.minimumLevels
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)