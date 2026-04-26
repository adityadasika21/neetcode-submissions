"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self): 
        self.newMap = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None : 
            return None 

        newHead = Node(head.val)
        self.newMap[head] = newHead
        newHead.next = self.copyRandomList(head.next)
        newHead.random = self.newMap.get(head.random)
        return newHead