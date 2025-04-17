from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniques = set()
        for word in words:
            current = []
            for letter in word:
                current.append(morse[ord(letter)-97])
            transform = "".join(current)
            if transform not in uniques:
                uniques.add(transform)
        return len(uniques)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.uniqueMorseRepresentations
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)