# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def add_at_head(head, val):
    traverse = head
    new_head = ListNode(val)
    cur = new_head
        
    while traverse:
        new_head.next = traverse
        traverse = traverse.next
        new_head = new_head.next
        
    return cur
    
    
def add_at_tail(head, val):
    traverse = head
        
        
        
        
    return head


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cur = head
        cur2 = head
        front_nodes = list()
        back_nodes = list()
        
        while cur2:
            if cur2.val == left:
                while cur2.val != right:
                    cur2 = cur2.next
            
            if cur2.val < left:
                front_nodes.append(cur2.val)
                    
            if cur2.val > right:
                back_nodes.append(cur2.val)
                
            cur2 = cur2.next
        
        while cur: 
            cur2 = cur
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
                cur = cur.next
        
        front_nodes = front_nodes[::-1]
        back_nodes = back_nodes[::-1]
        
        for i in range(len(front_nodes)):
            cur = add_at_head(cur, front_nodes[i])
        
        """
        for i in range(len(back_nodes)):
            add_at_tail(cur, back_nodes[i])
            
        """
        
        return cur
