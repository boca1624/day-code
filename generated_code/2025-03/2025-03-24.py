class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 示例：反转一个链表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

reversed_head = reverse_linked_list(head)

# 输出反转后的链表
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
