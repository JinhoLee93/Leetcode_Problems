# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = list()
        while head is not None:
            if head.val not in seen:
                seen.append(head.val)
                head = head.next
            else: 
                return True
            
        return False
                
