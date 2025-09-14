class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = ListNode(key, value)
        else:
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = ListNode(key, value)

    def find(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] =
