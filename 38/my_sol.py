from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = "1"
        for _ in range(n-1):
            current_string = self.rle(current_string)
        return current_string
    
    def rle(self, my_str:str)-> str:
        new_string_list = []
        lagged_character = None
        lag = 0
        for character in my_str:
            if lagged_character is None:
                lagged_character = my_str[0]
                lag=1
            else:
                if character == lagged_character:
                    lag += 1
                else:
                    new_string_list.append(str(lag) + str(lagged_character))
                    lag = 1
                    lagged_character = character
        new_string_list.append(str(lag) + str(character))
        return "".join(new_string_list)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.countAndSay
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)