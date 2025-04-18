from typing import List

# Speedup, but still too slow
class Solution3:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        test_grid = [[False]*cols for row in range(rows)]
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry:
                    # grid[i][j] = float("-inf")
                    test_grid[i][j] = True
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                tester = True
                if j + stampWidth < cols + 1 and i + stampHeight < rows + 1:
                    for right in range(stampWidth):
                        for down in range(stampHeight):
                            tester = tester and not bool(grid[i+down][j+right])
                    if tester:
                        for right in range(stampWidth):
                            for down in range(stampHeight):   
                                test_grid[i+down][j+right] = True 
        final_tester = True
        for row in test_grid:
            final_tester = final_tester and all(row)
        return final_tester 

# Works but is too slow
class Solution2:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry:
                    grid[i][j] = float("-inf")
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                accumulator = 0
                if j + stampWidth < cols + 1 and i + stampHeight < rows + 1:
                    for right in range(stampWidth):
                        for down in range(stampHeight):
                            accumulator += grid[i+down][j+right]
                    if accumulator > -1:
                        for right in range(stampWidth):
                            for down in range(stampHeight):   
                                grid[i+down][j+right] +=1  
        for row in grid:
            for entry in row:
                if entry == 0:
                    return False
        return True                   



# doesn't work, but is a good heuristic
class Solution1:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        occus = []
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry:
                    occus.append((i,j))
        if len(occus) == rows*cols:
            return True
        if stampWidth > cols or stampHeight > rows:
            return False
        occucopy = occus[:]
        # iterate over positions for horizontal and vertical limits
        while occus:
            candidate = occus.pop()
            min_left = stampWidth
            min_above = stampHeight
            min_right = stampWidth
            min_below = stampHeight
            min_left = min(min_left, candidate[1])
            min_above = min(min_above, candidate[0])
            min_right = min(min_right, cols - candidate[1] - 1)
            min_below = min(min_below, rows - candidate[0] - 1)
            for other in occucopy:
                if other != candidate:
                    # equal row
                    if candidate[0] == other[0]:
                        between = abs(candidate[1] - other[1])-1
                        if candidate[1] > other[1]:
                            min_left = min(min_left, between)
                        else:
                            min_right = min(min_right, between)
                    # equal column
                    elif candidate[1] == other[1]:
                        between = abs(candidate[0] - other[0])-1
                        if candidate[0]> other[0]:
                            min_above = min(min_above, between)
                        else:
                            min_below = min(min_below, between)           
            if 0 < min_above < stampHeight:
                return False
            if 0 < min_below < stampHeight:
                return False
            if 0 < min_left < stampWidth:
                return False
            if 0 < min_right < stampWidth:
                return False
        return True




        

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.possibleToStamp
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)