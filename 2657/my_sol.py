from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        occurence_set = set()
        counter = 0
        # C = [None]*len(A)
        for i in range(len(A)):
            if A[i] in occurence_set:
                counter +=1
            else:
                occurence_set.add(A[i])
            if B[i] in occurence_set:
                counter +=1
            else:
                occurence_set.add(B[i])
            A[i] = counter
        return A


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findThePrefixCommonArray
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)