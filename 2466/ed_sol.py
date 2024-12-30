# Approach 1

from typing import List

# Approach 1: Iterative Dynamic Programming 
class Solution1:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0]*(high)
        mod = 10**9+7
        for end in range(1,high+1):
            if end >= zero:
                dp[end] += dp[end - zero] % mod
            if end >= one:
                dp[end] += dp[end - one] % mod
        
        accumulator = 0
        for index in range(low, high+1):
            accumulator += dp[index]
        return accumulator % mod

class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.dp = [1] + [-1]*(high)
        mod = 10**9+7
        self.dfs(high, zero, one, mod)
        return sum(self.dp[low:(high+1)])
    def dfs(self, end, zero, one, mod):
        if self.dp[end] != -1:
            return self.dp[end]
        answer = 0
        if end >= zero:
            answer += self.dfs(end - zero, zero, one, mod) % mod
        if end >= one:
            answer += self.dfs(end - one, zero, one, mod) % mod
        self.dp[end] = answer % mod
        return self.dp[end]



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.countGoodStrings
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    solution_object = Solution2()
    solve_method = solution_object.countGoodStrings
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)