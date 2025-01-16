from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # second attempt, I think technically faster than first.
        if (len(nums2)%2 != 0):
            for i in range(1, len(nums1)):
                nums1[0] ^= nums1[i]
        else:
            nums1[0] = 0
        if (len(nums1)%2 != 0):
            for i in range(1, len(nums2)):
                nums2[0] ^= nums2[i]
        else:
            nums2[0] = 0
        return nums1[0] ^ nums2[0]
        # first attempt, works great!
        # first = 0
        # if (len(nums2)%2 != 0):
        #     for number in nums1:
        #         first ^= number
        # second = 0
        # if (len(nums1)%2 != 0):
        #     for number in nums2:
        #         second ^= number
        # return first ^ second

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.xorAllNums
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)