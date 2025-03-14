class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next
    next_node = current.next

    for _ in range(right - left):
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
        next_node = current.next

    return dummy.next
