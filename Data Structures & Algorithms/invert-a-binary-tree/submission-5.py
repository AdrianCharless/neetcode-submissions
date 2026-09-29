# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque 
        q = deque()
        if root:
            q.append(root)

        while q:
            curr = q.popleft()
            if curr.left is None and curr.right:
                curr.left = curr.right
                curr.right = None
                q.append(curr.left)
            elif curr.right is None and curr.left:
                curr.right = curr.left 
                curr.left = None
                q.append(curr.right)
            elif curr.right and curr.left:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                q.append(curr.left)
                q.append(curr.right)
        
        return root