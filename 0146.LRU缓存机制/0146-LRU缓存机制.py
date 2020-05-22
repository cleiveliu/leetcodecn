class DLinkedList(object):
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None


class LRUCache:
    def _add_node(self, node):
        """add a node to the right after head"""
        tail = self.head.next

        node.next = tail
        tail.prev = node

        node.prev = self.head
        self.head.next = node

    def _remove_node(self, node):
        """remove an exsting node from Dlinkedlist"""
        prev = node.prev
        tail = node.next

        prev.next = tail
        tail.prev = prev

        node.next = None
        node.prev = None

    def _move_to_head(self, node):
        """move an exsiting node to the place which is right after head"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """remove the last node"""
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        node = self.cache.get(key, None)

        if node == None:
            node = DLinkedList()
            node.key = key
            node.value = value
            self.cache[key] = node
            if self.size >= self.capacity:
                pop_node = self._pop_tail()
                del self.cache[pop_node.key]
                self._add_node(node)
            else:
                self._add_node(node)
                self.size += 1
        else:
            node.value = value
            self._remove_node(node)
            self._add_node(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
