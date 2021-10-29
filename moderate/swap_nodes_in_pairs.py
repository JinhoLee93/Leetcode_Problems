# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode(-1)
      dummy.next = head
      prv = dummy
      
      while head and head.next:
        odd = head
        even = head.next
        
        prv.next = even
        odd.next = even.next 
        even.next = odd
        prv = odd
        
        head = odd.next 
        
      return dummy.next
