# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cur = head
        front_nodes = list()
        end_nodes = list()

        while cur: 
            if cur.val == left:
                prv = None
                while cur.val != right: 
                    nxt = cur.next
                    cur.next = prv
                    prv = cur
                    cur = nxt
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt            
                cur = prv
                break
                
            else:
                front_nodes.append(cur.val)
                cur = cur.next
                
        head = cur
        
        return head
