# 设计一个链表类，并实现删除倒数第k个节点的功能

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def remove_kth_from_end(self, k):
        fast = slow = self.head
        for _ in range(k):
            if fast: fast = fast.next
        if not fast:
            self.head = self.head.next  # 删除头节点
            return
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

# 测试代码
ll = LinkedList()
for i in range(1, 6):  # 添加 1 -> 2 -> 3 -> 4 -> 5
    ll.add(i)

ll.print_list()  # 输出：5 -> 4 -> 3 -> 2 -> 1 -> None
ll.remove_kth_from_end(2)  # 删除倒数第二个
