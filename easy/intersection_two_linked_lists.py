# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        
        # two pointers will catch up after the first loop
        while p1 != p2: 
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
                
        return p1 
