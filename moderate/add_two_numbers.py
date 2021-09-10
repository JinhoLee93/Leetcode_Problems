# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(N + M), Space: O(N + M)
    def reverseList(self, l):
        prv = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
        return prv
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(-1)
        newPointer = newList
        
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        carry = 0
        while l1 and l2:
            value = l1.val + l2.val
            if value + carry > 9:
                newPointer.next = ListNode((value + carry) % 10)
                carry = 1
            
            else:
                newPointer.next = ListNode(value + carry)
                carry = 0
            
            newPointer = newPointer.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                if l1.val + carry > 9:
                    newPointer.next = ListNode((l1.val + carry) % 10)
                    carry = 1

                else:
                    newPointer.next = ListNode(l1.val + carry)
                    carry = 0

                newPointer = newPointer.next
                l1 = l1.next

        elif l2:
            while l2:
                if l2.val + carry > 9:
                    newPointer.next = ListNode((l2.val + carry) % 10)
                    carry = 1

                else:
                    newPointer.next = ListNode(l2.val + carry)
                    carry = 0

                newPointer = newPointer.next
                l2 = l2.next

        if carry == 1:
            newPointer.next = ListNode(carry)
            newPointer = newPointer.next
        
        res = newList.next
        res = self.reverseList(res)
        
        return res
