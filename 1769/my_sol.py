from typing import List


#  of               001011
# left carriers       5310
# left balls          3221
#                      i
# lb[i] = lb[i+1] + box[i]
# lc[i] = lc[i+1] + lb[i+1]

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        my_len = len(boxes)
        return_list = [0]*my_len
        # how many moves to carry everything of the right of i onto i
        left_carriers = [0]*my_len
        # how many balls there will be at i afterwards
        left_balls = [0]*my_len
        # how many moves to carry everything of the left of i onto i
        right_carriers = [0]*my_len
        # start with 0, because there's nothing left of index 0
        # how many balls there will be at i afterwards
        right_balls = [0]*my_len
        # start with edge count
        right_balls[0] = int(boxes[0])
        left_balls[-1] = int(boxes[-1])
        for index in range(1, my_len):
            right_carriers[index] = right_carriers[index-1] + right_balls[index-1] 
            right_balls[index] = right_balls[index-1] + int(boxes[index])
            return_list[index] += right_carriers[index]
            back_index = my_len - index - 1
            left_carriers[back_index] = left_carriers[back_index+1] + left_balls[back_index+1]
            left_balls[back_index] = left_balls[back_index+1] + int(boxes[back_index])
            return_list[back_index] += left_carriers[back_index]
        return return_list




if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.minOperations
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)