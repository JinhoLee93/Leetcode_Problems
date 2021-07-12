# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def traverse(head): 
    while head:
        print(head.val) 
        head = head.next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head: 
            return None 
        
        cur, prv = head, None
    
        while cur.val != left: 
            prv = cur
            cur = cur.next
            
        tail, con = cur, prv
        
        while cur.val != right: 
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
        nxt = cur.next 
        cur.next = prv
        prv = cur
        cur = nxt
        
        if con:
            con.next = prv
        
        else:
            head = prv
        
        tail.next = cur
        
        return head 
