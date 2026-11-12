# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque()
        q.append(root)
        res = []

        while q:
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                if i == lenQ - 1:
                    if node:
                        res.append(node.val)
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
        
        return res

                

