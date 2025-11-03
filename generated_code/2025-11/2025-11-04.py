class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.capacity = 1007
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = ListNode(key, True)
            self.size += 1
        else:
            while node:
                if node.key == key:
                    node.val = True
                    return
                if node.next is None:
                    node.next = ListNode(key, True)
                    self.size += 1
                    return
                node = node.next

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
                self.size -= 1
                return
            prev = node
            node = node.next

    def contains(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node
