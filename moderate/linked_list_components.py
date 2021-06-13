# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def check(head, nums):
    nums = sorted(nums)
    traverse = head
    disconnected = True
    connected = 0
    while traverse: 
        if traverse.val in nums:
            if disconnected:
                connected += 1
            disconnected = False
        else:
            disconnected = True


        traverse = traverse.next
        
    return connected

    
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        return check(head, nums)
