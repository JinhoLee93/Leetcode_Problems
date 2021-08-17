# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Brute Force: Time: O(NlogN), Space: O(N)
        newList = ListNode(-1)
        cur = newList
        tempList = []
        
        for l in lists:
            while l:
                tempList.append(l.val)
                l = l.next
                
        for num in sorted(tempList): 
            cur.next = ListNode(num)
            cur = cur.next
        
        return newList.next
