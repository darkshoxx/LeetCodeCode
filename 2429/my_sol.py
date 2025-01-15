from typing import List


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones = bin(num2)[2:].count("1")
        bin_num1 = bin(num1)[2:]
        my_len = len(bin_num1)
        if ones > my_len:
            return 2**ones - 1
        res_list = ["0"]*my_len
        index = 0
        while ones > 0 and index < my_len:
            if bin_num1[index] == "1":
                res_list[index] = "1"
                ones -= 1
            index += 1
        if ones > 0:
            index -= 1
        while ones > 0:
            if bin_num1[index] == "0":
                res_list[index] = "1"
                ones -=1
            index -= 1
        return int("".join(res_list),2)

        
            


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.minimizeXor
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)