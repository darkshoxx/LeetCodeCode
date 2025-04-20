from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        candidate = []
        result = self.traverse(root, candidate)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        matcher = [ alphabet[item] for item in reversed(result)]
        return "".join(matcher)
    def traverse(self, node, candidate):
        candidate.append(node.val)
        leaf = True
        single_branch = bool(node.left) ^ bool(node.right)
        if node.left:
            left_candidate = self.traverse(node.left, candidate[:])
            if single_branch:
                return left_candidate
            leaf = False
        if node.right:
            right_candidate = self.traverse(node.right, candidate[:])
            if single_branch:
                return right_candidate
            leaf = False
        
        if leaf:
            return candidate
        for left_entry, right_entry in zip(reversed(left_candidate), reversed(right_candidate)):
            if left_entry < right_entry:
                return left_candidate
            elif right_entry < left_entry:
                return right_candidate
        if len(left_candidate) < len(right_candidate):
            return left_candidate
        return right_candidate

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.findTargetSumWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)