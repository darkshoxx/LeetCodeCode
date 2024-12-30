from typing import List


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        reachable_ending_0 = [0]*(high + 1)
        reachable_ending_1 = [0]*(high + 1)
        mod = (10**9)+7
        current_0 = zero
        current_1 = one
        reachable_ending_0[current_0] = 1
        reachable_ending_1[current_1] = 1
        change_occured = True
        while change_occured:
            change_occured = False
            if current_0 + one <= high:
                reachable_ending_1[current_0 + one] += reachable_ending_0[current_0] % mod
                change_occured = True
            if current_1 + one <= high:
                reachable_ending_1[current_1 + one] += reachable_ending_1[current_1] % mod
                change_occured = True
            if current_0 + zero <= high:
                reachable_ending_0[current_0 + zero] += reachable_ending_0[current_0] % mod
                change_occured = True
            if current_1 + zero <= high:
                reachable_ending_0[current_1 + zero] += reachable_ending_1[current_1] % mod
                change_occured = True
            current_0 +=1
            current_1 +=1

        accumulator = 0
        for index in range(low, high+1):
            accumulator += reachable_ending_0[index] % mod
            accumulator += reachable_ending_1[index] % mod
        return accumulator % mod

        

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countGoodStrings
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)