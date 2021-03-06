# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prv = None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
            
        cur = prv
        
        return cur 
