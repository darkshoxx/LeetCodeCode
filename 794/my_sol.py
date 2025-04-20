from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        letters = "".join(board)
        o_count = letters.count("O")
        x_count = letters.count("X")
        x_win = 0
        o_win = 0
        if o_count > x_count or o_count < x_count - 1:
            return False
        for row in board:
            if row == "XXX":
                x_win +=1
            if row == "OOO":
                o_win +=1
        rot_board = [
            letters[0] + letters[3] + letters[6],
            letters[1] + letters[4] + letters[7],
            letters[2] + letters[5] + letters[8],
        ]
        for row in rot_board:
            if row == "XXX":
                x_win +=1
            if row == "OOO":
                o_win +=1
        diag_board = [
            letters[0] + letters[4] + letters[8],
            letters[2] + letters[4] + letters[6],
        ]
        for row in diag_board:
            if row == "XXX":
                x_win +=1
            if row == "OOO":
                o_win +=1   
        if x_win > 0 and x_count == o_count:
            return False
        if o_win > 0 and x_count == o_count+1:
            return False
        return True


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.validTicTacToe
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)