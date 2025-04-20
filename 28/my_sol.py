from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        candidates = []
        initial = needle[0]
        for index in range(len(haystack)):
            if haystack[index] == initial:
                candidates.append(index)
            for jndex in range(len(candidates)):
                if candidates[jndex] is not None:
                    if needle[index - candidates[jndex]] != haystack[index]:
                        candidates[jndex] = None
                    else:
                        if candidates[jndex] + len(needle) == index+1:
                            return candidates[jndex]
        return -1
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.strStr
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)