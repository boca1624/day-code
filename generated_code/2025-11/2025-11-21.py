class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = ListNode(key, value)
        else:
            while node.next:
                node = node.next
            node.next = ListNode(key, value)

    def get(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return node.value
            prev = node
            node = node.next
        return None
