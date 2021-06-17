# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        traverse = head
        palindrome = list()
        
        while traverse:
            palindrome.append(traverse.val)
            traverse = traverse.next
            
        if palindrome == palindrome[::-1]:
            return True
        
        else: 
            return False
