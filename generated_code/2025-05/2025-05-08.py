class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    reversed_list = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return reversed_list

# 测试递归反转链表
def print_linked_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# 示例链表: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("原链表:")
print_linked_list(head)

head = reverse_linked_list(head)
print("反转后的链表:")
print_linked_list(head)
