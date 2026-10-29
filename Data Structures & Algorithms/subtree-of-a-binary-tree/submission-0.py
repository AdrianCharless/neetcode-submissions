# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r, s):
            if r is None and s is None:
                return True
            elif r is None or s is None:
                return False
            elif r.val != s.val:
                return False
            else:
                return sameTree(r.left, s.left) and sameTree(r.right, s.right)

        if sameTree(root, subRoot):
            return True
        else:
            if root.left:
                return(self.isSubtree(root.left, subRoot))
            if root.right:
                return(self.isSubtree(root.right, subRoot))

        return False

            

        