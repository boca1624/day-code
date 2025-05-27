class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    reversed_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

# 示例链表: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 反转链表
reversed_head = reverse_linked_list(head)
