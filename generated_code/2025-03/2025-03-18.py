class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    next_node = None

    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

# 构造链表并测试
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(reverse_between(head, 2, 4))
