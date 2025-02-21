from typing import List, Optional
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        path = []
        target_found = False
        reduced_target = target
        while reduced_target != 0:
            if reduced_target % 2 == 1:
                path.append("L")
                reduced_target = (reduced_target - 1 )/2
            else:
                path.append("R")
                reduced_target = (reduced_target - 2 )/2

        node = self.root
        if path == []:
            target_found = True
        while not target_found:
            next_dir = path.pop()
            if next_dir == "L":
                node = node.left
            else:
                node = node.right
            if node is None:
                return False
            if path == []:
                target_found = True
        return True


if __name__ == "__main__":
    from examples import inputs, outputs
    for _input, output in zip(inputs, outputs):
        solution_object = Solution(_input[0])
        solve_method = solution_object.find
        check = solve_method(_input[1])
        print(check)

