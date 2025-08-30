class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = ListNode(key, value)
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = ListNode(key, value)

    def get(self, key):
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
                return True
            prev = node
            node = node.next
        return False
