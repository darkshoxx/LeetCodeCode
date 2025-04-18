from typing import List
from numpy import argmax
from numpy import argmax
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        gas, cost, lag = self.parallel_rle(gas, cost)
        n = len(cost)
        position = int((argmax(cost)+1) % n)
        for index in range(n):
            possible = self.circuit(gas, cost, lag, position, n)
            if possible:
                return sum(lag[:position])
            else:
                position = (position + 1) % n
        return -1
    
    def circuit(self, gas: List[int], cost: List[int], lag: List[int], position, n) -> bool:
        tank = 0 
        for index in range(n):
            tank += gas[position]*lag[position] - cost[position]*lag[position]
            if tank < 0:
                return False
            position = (position + 1) % n
        return True

    def parallel_rle(self, gas: List[int], cost: List[int])-> tuple[List, List, List]:
        new_gas_list = []
        new_cost_list = []
        lag_list = []
        lagged_gas = None
        lagged_cost = None
        lag = 0
        for index in range(len(cost)):
            if lagged_gas is None:
                lagged_gas = gas[0]
                lagged_cost = cost[0]
                lag = 1
            else:
                if gas[index] == lagged_gas and cost[index] == lagged_cost:
                    lag += 1
                else:
                    new_gas_list.append(lagged_gas)
                    new_cost_list.append(lagged_cost)
                    lag_list.append(lag)
                    lag = 1
                    lagged_gas = gas[index]
                    lagged_cost = cost[index]
        new_gas_list.append(lagged_gas)
        new_cost_list.append(lagged_cost)
        lag_list.append(lag)
        return new_gas_list, new_cost_list, lag_list


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.canCompleteCircuit
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)