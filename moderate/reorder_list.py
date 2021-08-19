# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(N), Space: O(N)
        middle = head
        fast = head
        
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        
        second = middle.next 
        middle.next = None
        prv = None
        while second:
            nxt = second.next
            second.next = prv
            prv = second
            second = nxt
            
        l1, l2 = head, prv
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2
