from typing import List

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # recreate stack solution from editorial

    ## Fast, but wrong
    # from functools import cache
    # def canBeValid(self, s: str, locked: str) -> bool:
    #     difference = 0
    #     flip_indices = []
    #     for index in range(len(s)):
    #         letter = s[index]
    #         lock = locked[index]
    #         if letter == "(":
    #             difference +=1
    #         else:
    #             difference -=1
    #         if difference < 0:
    #             if lock == "1":
    #                 return False
    #             else:
    #                 flip_indices.append(index)
    #                 difference = 1
    #     s = "".join(s[index] if index not in flip_indices else self.opp(s[index]) for index in range(len(s)))
    #     locked = "".join(locked[index] if index not in flip_indices else self.opp(locked[index]) for index in range(len(s)))
    #     difference = 0
    #     flip_indices = []
    #     for rev_index in range(len(s)):
    #         index = len(s) - rev_index - 1
    #         letter = s[index]
    #         lock = locked[index]
    #         if letter == ")":
    #             difference +=1
    #         else:
    #             difference -=1
    #         if difference < 0:
    #             if lock == "1":
    #                 return False
    #             else:
    #                 flip_indices.append(index)
    #                 difference = 1 
    #     s = "".join(s[index] if index not in flip_indices else self.opp(s[index]) for index in range(len(s)))
    #     return self.is_valid(s)       

    # def opp(self, char):
    #     if char == "(":
    #         return ")"
    #     if char == ")":
    #         return "("
    #     if char == "0":
    #         return "1"
    #     if char == "1":
    #         return "0"

    # @cache    
    # def is_valid(self, s:str):
    #     my_len = len(s)
    #     opened = s.count("(")
    #     closed = s.count(")")
    #     if opened != closed:
    #         return False
    #     if my_len < 3:
    #         if s == "()":
    #             return True
    #         return False
    #     else:
    #         if s[0] == "(" and s[-1] == ")":
    #             if self.is_valid(s[1:-1]):
    #                 return True
    #         if my_len > 3:
    #             valid = False
    #             sep = 2
    #             while (not valid) and sep < my_len -1:
    #                 valid = self.is_valid(s[:sep]) and self.is_valid(s[sep:])
    #                 sep += 1
    #             return valid
    #     return False



    ## Faster, but still too slow
    # from functools import cache
    # @cache
    # def canBeValid(self, s: str, locked: str) -> bool:
    #     my_len = len(s)
    #     if my_len <3:
    #         return self.double_check(s, locked)
    #     outside_s = s[0] + s[-1]
    #     outside_l = locked[0] + locked[-1]
    #     if self.double_check(outside_s, outside_l):
    #         if self.canBeValid(s[1:-1], locked[1:-1]):
    #             return True
    #     if my_len > 3:
    #         valid = False
    #         sep = 2
    #         while (not valid) and sep < my_len -1:
    #             valid = self.canBeValid(s[:sep], locked[:sep]) and self.canBeValid(s[sep:], locked[sep:])
    #             sep += 1
    #         return valid
    #     return False
    
    # @cache
    # def double_check(self, s, locked):
    #     if s == "()":
    #         return True
    #     if locked == "00":
    #         return True
    #     if s == "((" and locked == "10":
    #         return True
    #     if s == "))" and locked == "01":
    #         return True
    #     return False

    ## Too slow
    # def canBeValid(self, s: str, locked: str) -> bool:
    #     zeroes = locked.count("0")
    #     opened = s.count("(")
    #     closed = s.count(")")
    #     if abs(opened-closed)/2 > zeroes:
    #         return False
    #     if zeroes == 0:
    #         return self.is_valid(s)
    #     # if self.is_valid(s):
    #     #     return True
    #     split_index = locked.find("0")
    #     open_string = s[:split_index] + "(" + s[split_index+1:]
    #     closed_string = s[:split_index] + ")" + s[split_index+1:]
    #     new_locked = locked[:split_index] + "1" + locked[split_index+1:]
    #     return self.canBeValid(open_string, new_locked) or self.canBeValid(closed_string, new_locked)

        
        
    # @cache    
    # def is_valid(self, s:str):
    #     my_len = len(s)
    #     opened = s.count("(")
    #     closed = s.count(")")
    #     if opened != closed:
    #         return False
    #     if my_len < 3:
    #         if s == "()":
    #             return True
    #         return False
    #     else:
    #         if s[0] == "(" and s[-1] == ")":
    #             if self.is_valid(s[1:-1]):
    #                 return True
    #         if my_len > 3:
    #             valid = False
    #             sep = 2
    #             while (not valid) and sep < my_len -1:
    #                 valid = self.is_valid(s[:sep]) and self.is_valid(s[sep:])
    #                 sep += 1
    #             return valid
    #     return False

            

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.canBeValid
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)