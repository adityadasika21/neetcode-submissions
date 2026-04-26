# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        temp = []
        for lst in lists: 
            while lst: 
                temp.append(lst.val)
                lst = lst.next

        temp.sort()
        
        newHead = ListNode(0)
        curr = newHead

        for node in temp :
            curr.next = ListNode(node)
            curr = curr.next

        return newHead.next