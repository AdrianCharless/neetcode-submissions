# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxSoFar, node):
            if not node:
                return 0
            if node.val >= maxSoFar:
                res = 1
            else:
                res = 0
            maxSoFar = max(maxSoFar, node.val)
            res += dfs(maxSoFar, node.left)
            res += dfs(maxSoFar, node.right)
            return res

        return dfs(root.val, root)
            
