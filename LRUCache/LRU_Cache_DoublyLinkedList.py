class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        nextNode.prev = node
        node.prev = self.head

    def deleteNode(self, node):
        prev = node.prev
        node.prev.next = node.next
        node.next.prev = prev

    def delete(self):
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.map = {}
        self.list = DoubleLinkedList()
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self.list.deleteNode(self.map[key])
            self.list.insert(self.map[key])
            return self.map[key].val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.list.deleteNode(self.map[key])
            del self.map[key]
            self.count -= 1
        if self.count == self.size:
            n = self.list.delete()
            del self.map[n.key]
            self.count -= 1
        node = Node(value, key)
        self.list.insert(node)
        self.map[key] = node
        self.count += 1


lru = LRUCache(2)
lru.put(1, 100)
lru.put(2, 200)
lru.put(3, 300)
print(lru.get(2))  # 200
lru.put(4, 200)
print(lru.get(3))  # -1 
print(lru.get(2))  # 200
