from typing import List, Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dash_list = self.dashes(traversal)
        numbers = [item.strip("-") for item in traversal.split("-")]
        
    def dashes(self, traversal):
        dash_list = []
        new_entry = True
        for i in traversal:
            if new_entry:
                if i != "-":
                    continue
                else:
                    dash_list.append(1)
            else:
                if i == "-":
                    dash_list[-1] += 1
                else:
                    continue
        return dash_list

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.recoverFromPreorder
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)