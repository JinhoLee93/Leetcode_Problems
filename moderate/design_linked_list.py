class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        traverse = self.head
        while traverse:
            if i == index:
                return traverse.val

            i += 1
            traverse = traverse.next_node

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head.val == None:
            self.head.val = val
        else:
            traverse_old = self.head
            new_list = MyLinkedList()
            new_list.head.val = val
            traverse_new = new_list.head

            while traverse_old:
                traverse_new.next_node = traverse_old
                traverse_old = traverse_old.next_node
                traverse_new = traverse_new.next_node

            self.head = new_list.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.head.val == None:
            self.head.val = val
        else:
            traverse = self.head
            while traverse.next_node:
                traverse = traverse.next_node
            traverse.next_node = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        traverse_old = self.head
        new_list = MyLinkedList()
        traverse_new = new_list.head

        i = 0
        while traverse_old:
            if index == i:
                traverse_new.val = new_node.val
                if traverse_old:
                    traverse_new.next_node = Node(None)
                    traverse_new = traverse_new.next_node
            else:
                traverse_new.val = traverse_old.val
                traverse_old = traverse_old.next_node
                if traverse_old:
                    traverse_new.next_node = Node(None)
                    traverse_new = traverse_new.next_node
            i += 1

        if index == i:
            new_list.addAtTail(val)

        self.head = new_list.head

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        traverse_old = self.head
        traverse_num = self.head
        new_list = MyLinkedList()
        traverse_new = new_list.head

        j = 0
        while traverse_num:
            traverse_num = traverse_num.next_node
            j += 1

        j -= 1

        i = 0
        while traverse_old:
            if index == i:
                traverse_old = traverse_old.next_node
            else:
                traverse_new.val = traverse_old.val
                traverse_old = traverse_old.next_node
                if traverse_old:
                    if index == j and i == j - 1:
                        break
                    else:
                        traverse_new.next_node = Node(None)
                        traverse_new = traverse_new.next_node

            i += 1
        self.head = new_list.head
