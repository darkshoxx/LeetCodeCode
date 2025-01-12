# Approach 1

from typing import List


class Solution1:
    def canBeValid(self, s: str, locked: str) -> bool:
        my_len = len(s)
        if my_len % 2 == 1:
            return False
        open_brackets = []
        unlocked = []
        for i in range(my_len):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if len(open_brackets) > 0:
                    open_brackets.pop()
                elif len(unlocked):
                    unlocked.pop()
                else:
                    return False
        while open_brackets and unlocked and open_brackets[-1]< unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        
        if open_brackets:
            return False
        return True

class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        my_len = len(s)
        if my_len % 2 == 1:
            return False
        open_brackets = 0
        unlocked = 0        
        for i in range(my_len):
            if locked[i] == "0":
                unlocked += 1
            elif s[i] == '(':
                open_brackets += 1
            elif s[i] == ")":
                if open_brackets > 0:
                    open_brackets -= 1
                elif unlocked > 0:
                    unlocked -= 1
                else:
                    return False
        balance = 0
        for j in range(my_len): 
            i = my_len - j - 1
            if locked[i] == '0':
                balance -= 1
                unlocked -= 1
            if s[i] == '(':
                balance += 1
                open_brackets -= 1
            if s[i] == ')':
                balance -= 1
            if balance > 0:
                return False
            if unlocked == 0 and open_brackets == 0:
                break
        if open_brackets > 0:
            return False
        return True
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.canBeValid
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    solution_object = Solution2()
    solve_method = solution_object.canBeValid
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)