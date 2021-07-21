# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new = ListNode(next=head)
        prv, cur = new, head
        
        while cur:
            nxt = cur.next
            
            if cur.val == val:
                prv.next = nxt
            
            else:
                prv = cur
            
            cur = nxt
        
        return new.next
