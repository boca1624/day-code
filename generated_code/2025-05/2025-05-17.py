# 设计一个链表类，支持链表反转和循环链表检测
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # 添加节点
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 反转链表
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 检测链表是否有环
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 打印链表
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# 测试
ll =
