from queue import PriorityQueue
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
        
        class Wrapper:
            def __init__(self, node):
                self.node = node
                
            def __lt__(self, other):
                return self.node.val < other.node.val 
            
        pq = PriorityQueue() 
        head = pointer = ListNode(-1) 
        
        for l in lists:
            if l:
                pq.put(Wrapper(l))
        
        while not pq.empty():
            node = pq.get().node
            pointer.next = node
            pointer = pointer.next
            node = node.next
            if node:
                pq.put(Wrapper(node))
                
        return head.next
