# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first, second, added = [], [], []
        f, s, t = l1, l2, ListNode(-1, None)
        
        while f:
            first.append(f.val)
            f = f.next 
        
        while s:
            second.append(s.val)
            s = s.next
        
        if len(first) < len(second):
            first, second = second, first
            
        long, short = len(first), len(second)
        carry = 0
        
        for i in range(short):
            s = first[i] + second[i] + carry
            carry = 0
            if s >= 10:
                carry += 1
                added.append(s - 10)
            
            else:
                carry = 0
                added.append(s)
                
        for i in range(short, long):
            s = first[i] + carry
            carry = 0
            if s >= 10:
                carry += 1
                added.append(s - 10)
            
            else:
                carry = 0
                added.append(s)
        
        if carry > 0:
            added.append(carry)
        
        ap = t
        for i in range(len(added)): 
            ap.next = ListNode(added[i])
            ap = ap.next
            
        return t.next
