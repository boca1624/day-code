class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = ListNode(key, value)
        else:
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = ListNode(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                return
            prev =
