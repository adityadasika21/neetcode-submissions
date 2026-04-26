# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: 
            return res

        def dfsRight(root, level): 
            if not root: 
                return None

            if level == len(res): 
                res.append(root.val)            

            dfsRight(root.right, level+1)
            dfsRight(root.left, level+1)

        dfsRight(root,0) 
        return res