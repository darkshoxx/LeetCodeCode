# Approach 1

from typing import List, Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pass
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.recoverFromPreorder
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)