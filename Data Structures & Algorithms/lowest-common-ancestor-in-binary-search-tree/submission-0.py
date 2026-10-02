# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = root
        curr = root
        pPath =[]
        qPath = []
        while curr.val != p.val:
            if curr.val > p.val:
                pPath.append(curr)
                curr = curr.left
            else:
                pPath.append(curr)
                curr = curr.right
        pPath.append(p)
        curr = root
        while curr.val != q.val:
            if curr.val > q.val:
                qPath.append(curr)
                curr = curr.left
            else:
                qPath.append(curr)
                curr = curr.right
        qPath.append(q)
        pi = len(pPath) - 1
        qi = len(qPath) - 1
        if len(qPath) > len(pPath):
            diff = len(qPath) - len(pPath)
            qi = len(qPath) - 1 - diff
        elif len(qPath) < len(pPath):
            diff = len(pPath) - len(qPath)
            pi = len(pPath) - 1 - diff
        
        while qPath[qi] != pPath[pi]:
            qi -= 1
            pi -= 1
        
        return qPath[qi]
        

        


