from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_history = []
        push_index = 0
        for entry in popped:
            if entry not in push_history:
                for i in range(push_index, pushed.index(entry)+1):
                    stack.append(pushed[push_index])
                    push_history.append(pushed[push_index])
                    push_index +=1
                stack.pop()
            else:
                if stack[-1] == entry:
                    stack.pop()
                else: 
                    return False
        return True

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.validateStackSequences
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)