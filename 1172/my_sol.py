from typing import List

# second attempt, faster, but still too slow.
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = {0:[]}
        self.capacity = capacity
        self.free_index = 0
        self.to_pop = -1

    def push(self, val: int) -> None:
        self.stack[self.free_index].append(val)
        new_index_set = False
        for index in range(self.free_index,len(self.stack)):
            if len(self.stack[index]) < self.capacity:
                self.free_index = index
                new_index_set = True
                break
        if not new_index_set:
            self.free_index = len(self.stack)
            self.stack[len(self.stack)] = []
        for index in reversed(range(len(self.stack))):
            if self.stack[index] != []:
                self.to_pop = index
                break
        
    def pop(self) -> int:
        if self.to_pop == -1:
            return -1
        val = self.stack[self.to_pop].pop()
        if self.free_index > self.to_pop:
            self.free_index = self.to_pop
        buffer_to_pop = self.to_pop
        self.to_pop = -1
        for index in reversed(range(buffer_to_pop+1)):
            if self.stack[index] != []:
                self.to_pop = index
                break      
        return val  


    def popAtStack(self, index: int) -> int:
        val = -1
        if index in self.stack:
            if self.stack[index]!= []:
                val = self.stack[index].pop()
        if index < self.free_index:
            self.free_index = index
        if index == self.to_pop and self.stack[index] == []:
            assigned = False
            for jndex in reversed(range(self.to_pop)):
                if self.stack[jndex] != []:
                    self.to_pop = jndex
                    assigned = True
                    break
            if not assigned:
                self.to_pop = -1
        return val

# first attempt, probably works, but too slow
class DinnerPlates1:
    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity
        

    def push(self, val: int) -> None:
        pushed = False
        for index in range(len(self.stack)):
            if len(self.stack[index])<self.capacity:
                self.stack[index].append(val)
                pushed = True
                break
        if not pushed:
            self.stack.append([val])
        

    def pop(self) -> int:
        for entry in reversed(self.stack):
            if entry != []:
                return entry.pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if index <= len(self.stack):
            if self.stack[index] != []:
                return self.stack[index].pop()
        return -1

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)