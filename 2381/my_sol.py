from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Attempt 4: Solaris428 Hints (sweep line)
        # iterations, prefix_reg
        # 0 [0 , 0 ,  0]
        # 1 [-1, 0 ,  1]
        # 2 [-1, 1 ,  1]
        # 3 [0 , 1 ,  1]
        # I = [0,0,0,1,1,1,0,0,0]
        # dI= [0,0,0,1,0,0,-1,0,0]
        # sr [0 ,1, 2]
        prefix_register = [0]*len(s)
        for sequence in shifts:
            if sequence[2]==1:
                offset = 1
            else:
                offset = -1
            prefix_register[sequence[0]] += offset
            if sequence[1]+1 < len(s):
                prefix_register[sequence[1]+1] -= offset
        shift_register = [prefix_register[0]]
        for index in range(1, len(s)):
            shift_register.append(shift_register[index-1]+ prefix_register[index])
        letters = [chr((ord(letter) + offset - ord('a'))%26 + ord("a"))
                   for letter, offset in zip(s,shift_register)
                   ]
        return "".join(letters)
        # Attempt 3: Still too slow
        # shift_register = [0]*len(s)
        # for index in range(len(s)):
        #     for sequence in shifts:
        #         if sequence[2]==1:
        #             offset = 1
        #         else:
        #             offset = -1
        #         if sequence[0] <= index <= sequence[1]:
        #             shift_register[index] += offset
        # letters = [chr((ord(letter) + offset - ord('a'))%26 + ord("a"))
        #            for letter, offset in zip(s,shift_register)
        #            ]
        # return "".join(letters)
    

        # Attempt 2: Too complicated
        # combing intervals [a,b,c] and [d,e,f] WLOG a<=d
        # ---a--b-d---e---
        # if b<d: add disjoint [a,b,c], [d,e,f]
        # --d--o--b for intersection o
        # if a==e: [d, e-1, f], [o, o, c+f], [a+1, b, c]
        # a--o--e for intersection o
        # if d==b: [a, b-1, c], [o, o, c+f], [d+1, e, f]
        # a--d-b--e
        # if a<d<b<e: [a, d-1, c], [d,b, c+f], [b+1, e, f]
        # 




        # Attempt 1: Too Slow
        # shift_register = [0]*len(s)
        # for sequence in shifts:
        #     if sequence[2]==1:
        #         offset = 1
        #     else:
        #         offset = -1
        #     for index in range(sequence[0], sequence[1]+1):
        #         shift_register[index] += offset
        # letters = [chr((ord(letter) + offset - ord('a'))%26 + ord("a"))
        #            for letter, offset in zip(s,shift_register)
        #            ]
        # return "".join(letters)
        

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.shiftingLetters
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)