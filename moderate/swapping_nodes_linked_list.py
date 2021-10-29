# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        length = 0
        tmp = None
        while first:
            length += 1
            if length == k:
                tmp = first

            first = first.next
        
        second = head
        tmp2 = None
        target = length - (k - 1)
        pos = 0
        while second:
            pos += 1
            if pos == target:
                tmp2 = second
                
            second = second.next
        
        tmp.val, tmp2.val = tmp2.val, tmp.val
            
        return head
