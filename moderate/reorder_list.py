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
        # Time: O(N), Space: O(1)
        
        # Find the middle
        middle = head
        fast = head
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next 
            
        # Reverse the second half
        prv = None
        while middle:
            nxt = middle.next
            middle.next = prv
            prv = middle
            middle = nxt
        
        # Merge the two lists
        first, second = head, prv
        while second.next:
            nxt = first.next
            first.next = second
            first = nxt
            
            nxt = second.next
            second.next = first
            second = nxt
