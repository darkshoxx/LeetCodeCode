from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern)
        available_num = list(range(1,length+2))

        done = False
        a_position = 0
        # r_position = 0
        p_position = 0
        response = []
        while not done:
            if pattern[p_position] == "I":
                response.append(available_num[a_position])
                a_position += 1
                p_position += 1
            else:
                next_index = p_position
                while next_index < length and pattern[next_index] == "D":
                    next_index += 1
                D_count =   next_index - p_position
                for index in range(a_position + D_count, a_position - 1, -1):
                    response.append(available_num[index])
                a_position += D_count + 1
                p_position += D_count + 1
            if p_position == length and pattern[-1] == "I":
                response.append(available_num[-1])
            if len(response) == length + 1:
                done = True
        response = [str(i) for i in response]
        return "".join(response)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.smallestNumber
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)