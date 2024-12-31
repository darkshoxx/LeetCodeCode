# Approach 1

from typing import List


class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs
        self.dp = [-1]*(days[-1]+1)
        self.is_travel_needed = {day for day in days}
        ret_val = self.solve(curr_day=1)
        return ret_val
    def solve(self, curr_day):
        if curr_day > self.days[-1]:
            return 0
        if curr_day not in self.is_travel_needed:
            return self.solve(curr_day+1)
        if self.dp[curr_day] != -1:
            return self.dp[curr_day]
        one_day = self.costs[0] + self.solve(curr_day+1)
        seven_day = self.costs[1] + self.solve(curr_day+7)
        thirty_day = self.costs[2] + self.solve(curr_day+30)
        self.dp[curr_day] = min(one_day, seven_day, thirty_day)
        return self.dp[curr_day]

class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        i = 0
        for day in range(1, days[-1]+1):
            if day < days[i]:
                dp[day] = dp[day-1]
            else:
                dp[day] = min(costs[0]+dp[day-1], costs[1] + dp[max(0,day-7)], costs[2] + dp[max(0,day-30)])
                i += 1
        return dp[days[-1]]

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.mincostTickets
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)
    solution_object = Solution2()
    solve_method = solution_object.mincostTickets
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)