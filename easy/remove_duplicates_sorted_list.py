# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        cur = head
        new = ListNode(None)
        re = new
        
        while cur:
            if cur.next:
                if cur.val == cur.next.val:
                    new.val = cur.val
                    while cur.val == cur.next.val:
                        cur = cur.next
                        if cur.next == None:
                            break
                    
                    cur = cur.next

                else:
                    new.val = cur.val
                    cur = cur.next
            
            else:
                new.val = cur.val
                cur = cur.next
            
            if cur:
                new.next = ListNode(None)
                new = new.next
     
            
        return re
