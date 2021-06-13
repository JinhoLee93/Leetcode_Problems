# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        traverse = head
        while traverse.val: 
            if traverse.val == left:
                prv = None
                cur = traverse  
                nxt = None
                while traverse.val != right: 
                    nxt = traverse.next
                    traverse.next = cur
                    prv = traverse
                traverse = prv
            
            else:
                traverse = traverse.next
        
        return traverse
