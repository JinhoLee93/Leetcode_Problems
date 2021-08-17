# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      # Time: O(N), Space: O(1), Two Pass
        lengthHead = 0
        headCur = head
        
        while headCur:
            lengthHead += 1
            headCur = headCur.next
            
        target = lengthHead - n
        
        newList = ListNode(-1)
        newCur = newList
        
        i = 0
        while head:
            if i == target:
                head = head.next
                
            else:
                newCur.next = ListNode(head.val)
                newCur = newCur.next
                head = head.next
            
            i += 1
        
        return newList.next
        
      # One pass, Same time and space
        newList = ListNode(0, head)
        left = newList
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        
        return newList.next
