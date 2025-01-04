# Approach 1

from typing import List


class Solution1:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for letter in letters:
            i = -1
            j = 0
            for k in range(0, len(s)):
                if s[k] == letter:
                    if i== -1:
                        i = k
                    j = k
            between = set()
            for k in range(i+1, j):
                between.add(s[k])
            ans += len(between)
        return ans

class Solution2:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1]*26
        last = [-1]*26
        ans = 0
        for k in range(len(s)):
            ord_ind = self.l_to_n(s[k])
            if first[ord_ind] == -1:
                first[ord_ind] = k
            last[ord_ind] = k
        for i in range(26):
            if first[i] != -1:
                first_ind = first[i]
                last_ind = last[i]
                between = set()
                for letter_index in range(first_ind+1, last_ind):
                    between.add(s[letter_index])
                ans += len(between)
        return ans
    def l_to_n(self, letter):
        return ord(letter) - ord("a")



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.countPalindromicSubsequence
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution2()
    solve_method = solution_object.countPalindromicSubsequence
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]

    print(checks)