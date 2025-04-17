from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for index in range(len(arr)-m+1):
            window_start = index
            window_end = m - 1 + index
            candidate = arr[window_start:window_end+1]
            possible = True
            for jndex in range(k-1):
                if possible:
                    if candidate == arr[window_start+m*(jndex+1):window_end+m*(jndex+1)+1]:
                        pass
                    else:
                        possible = False
            if possible:
                return True
        return False

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.containsPattern
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)