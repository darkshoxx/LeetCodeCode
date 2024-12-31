from typing import List


class Solution:
    #doesn't work
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs
        cheapest_prev = [2]
        cost_index_map:list = [0]
        self.length_list = [1, 7, 30]
        for index in range(1,len(days)):
            cost_index_map = self.cheapest(index, cheapest_prev[index-1], cost_index_map)
            cheapest_prev.append(sum([self.costs[cost_index] for cost_index in cost_index_map]))
        return cheapest_prev[-1]
    def cheapest(self, index, cost_limit, cost_index_map:list):
        current_list = self.days[:(index+1)]
        # check if ticket is already included
        day_index = 0
        days_covered = 0
        for index in cost_index_map:
            current_length = self.length_list[index]
            days_covered += current_length
            while current_list[day_index] < days_covered:
                day_index +=1
                if day_index == len(current_list) - 1:
                    # everything's already covered
                    return cost_index_map
        cost_index_map.append(0)


        # check if going a ticket up saves money
        cutoff = current_list[-1] - 7+0.5
        # find the index in the cost_index_map k such that the days up to cutoff are covered
        position_day_index = 0
        for index in cost_index_map:
            if position_day_index > cutoff:
                required_index = index - 1
                break
            current_length = self.length_list[index]
            current_start_day = current_list[position_day_index]
            next_required_ticket_day = current_start_day + current_length
            while current_list[position_day_index] < next_required_ticket_day:
                position_day_index +=1
            if position_day_index > cutoff:
                required_index = index
                break
        unchanged_cost = sum([self.costs[cost_index] for cost_index in cost_index_map])
        changed_cost = sum([self.costs[cost_index] for cost_index in cost_index_map if cost_index <= required_index]) + self.costs[1]
        if unchanged_cost > changed_cost:
            cost_index_map = [cost_index for cost_index in cost_index_map if cost_index <= required_index] + [1]
        # check if going two tickets up saves money
        cutoff = current_list[-1] - 30+0.5
        # find the index in the cost_index_map k such that the days up to cutoff are covered
        position_day_index = 0
        for index in cost_index_map:
            if position_day_index > cutoff:
                required_index = index - 1
                break
            current_length = self.length_list[index]
            current_start_day = current_list[position_day_index]
            next_required_ticket_day = current_start_day + current_length
            while current_list[position_day_index] < next_required_ticket_day:
                position_day_index +=1
            if position_day_index > cutoff:
                required_index = index
                break
        unchanged_cost = sum([self.costs[cost_index] for cost_index in cost_index_map])
        changed_cost = sum([self.costs[cost_index] for cost_index in cost_index_map if cost_index <= required_index]) + self.costs[2]
        if unchanged_cost > changed_cost:
            cost_index_map = [cost_index for cost_index in cost_index_map if cost_index <= required_index] + [2]
        return cost_index_map
        

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.mincostTickets
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)