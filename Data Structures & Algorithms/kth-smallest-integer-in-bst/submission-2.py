# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        maxHeap = []

        def traverse (root): 
            if not root: 
                return None

            traverse(root.left)
            heapq.heappush(maxHeap, root.val)
            traverse(root.right)
        traverse(root)
        return maxHeap[k-1]