# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        result = 0

        q = deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                current_root = q.popleft()
                if current_root.left:
                    q.append(current_root.left)
                if current_root.right:
                    q.append(current_root.right)
                    
            result += 1

        return result