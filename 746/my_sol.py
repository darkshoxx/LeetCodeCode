from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])
   

class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [None]*len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2,len(cost)):
            min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]
        return min(min_cost[-1], min_cost[-2])



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.minCostClimbingStairs
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)