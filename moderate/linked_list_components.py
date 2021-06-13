# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def check(head, nums):
    traverse = head
    while traverse: 
        print(traverse.val)
        traverse = traverse.next
    
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        check(head, nums)
