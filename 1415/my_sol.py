from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        init_dict = {
            1:"a",
            2:"b",
            3:"c",
        }
        next_small = {
            "a":"b",
            "b":"a",
            "c":"a"
        }
        next_large = {
            "a":"c",
            "b":"c",
            "c":"b"
        }
        import math
        leng = 3*2**(n-1)
        if k > leng:
            return ""

        result = []
        chunk = int(leng/3)
        res = math.ceil(k/chunk)
        init = init_dict[res]
        prev = init
        result.append(prev)
        for _ in range(n-1):
            rem = ((k-1) % chunk)+1
            chunk = int(chunk/2)
            if rem <= chunk:
                prev = next_small[prev]
                result.append(prev)
            else:
                prev = next_large[prev]
                result.append(prev)
        return "".join(result)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.getHappyString
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)