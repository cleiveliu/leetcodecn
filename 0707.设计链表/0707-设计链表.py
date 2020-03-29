class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index <=0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        else:
            cur = self.head
            while index - 1 > 0:
                cur = cur.next
                index -= 1
            node = Node(val)
            tail = cur.next
            cur.next = node
            node.next = tail
            tail.pre = node
            node.pre = cur
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            cur = self.head
            self.head = self.head.next
            self.head.pre = None
            del cur
        else:
            cur = self.head
            index_copy = index
            while index-1 > 0:
                cur = cur.next
                index -= 1
            if index_copy == self.length - 1:
                self.tail.pre = None
                self.tail = cur
                self.tail.next = None
            else:
                tail = cur.next.next
                cur.next.next = None
                cur.next.pre = None
                cur.next = tail
                tail.pre = cur
        self.length -= 1

    def __repr__(self):
        xs = []
        cur = self.head
        while cur:
            xs.append(cur.val)
            cur = cur.next
        return str(xs)
    __str__ = __repr__


            
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)