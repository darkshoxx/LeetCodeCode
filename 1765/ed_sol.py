# Approach 1

from typing import List


class Solution1:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        self.height = len(isWater)
        self.width = len(isWater[0])
        row = [-1]*len(isWater[0])
        heights = [row[:] for _ in isWater]
        current_level = []
        current_height = 0
        for i_row in range(len(isWater)):
            for j_col in range(len(isWater[i_row])):
                if isWater[i_row][j_col] == 1:
                    current_level.append((j_col,i_row))
                    heights[i_row][j_col] = current_height
        while current_level != []:
            current_height += 1
            next_level = []
            for x,y in current_level:
                for n_x, n_y in self.neighbours(x,y):
                    if heights[n_y][ n_x] == -1:
                        next_level.append((n_x, n_y))
                        heights[n_y][n_x] = current_height
            current_level = next_level
        print(heights)
        print(isWater)
        return heights
    
    def neighbours(self, x, y):
        n_list = []
        for delta_x in (-1,1):
            if 0 <= x+delta_x < self.width:
                n_list.append((x+delta_x,y))
        for delta_y in (-1,1):
            if 0 <= y+delta_y < self.height:
                n_list.append((x,y+delta_y))
        return n_list


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.highestPeak
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]

    print(checks)