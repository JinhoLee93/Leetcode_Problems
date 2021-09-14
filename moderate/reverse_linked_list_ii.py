# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        pointer = head
        beforeList = ListNode(-1)
        before = beforeList
        leftList = ListNode(-1)
        l = leftList
        endList = ListNode(-1)
        endPointer = endList
        
        while pointer:
            if count < left:
                before.next = ListNode(pointer.val)
                before = before.next
                pointer = pointer.next
                
            elif count == left:
                l.next = ListNode(pointer.val)
                l = l.next
                pointer = pointer.next
                
                while count < right:
                    l.next = ListNode(pointer.val)
                    l = l.next
                    pointer = pointer.next
                    count += 1
                
                prv = None
                cur = leftList.next
                while cur:
                    nxt = cur.next
                    cur.next = prv
                    prv = cur
                    cur = nxt
                
                connect = prv
                while connect.next:
                    connect = connect.next
                
                while pointer:
                    endPointer.next = ListNode(pointer.val)
                    endPointer = endPointer.next
                    pointer = pointer.next
                
                connect.next = endList.next
                leftList = prv
                
                break
        
            count += 1
        
        if left == 1:
            
            return leftList
        
        else:
            #beforeList = beforeList.next
            before.next = leftList
        
            return beforeList.next
