# 反转链表中部分节点（位置 m 到 n）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before reversal starts
    for _ in range(m - 1):
        prev = prev.next

    # Start reversal
    reverse_prev = prev
    current = prev.next
    prev_node = None
    for _ in range(n - m + 1):
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node

    # Connect reversed part back to the list
    reverse_prev.next.next = current
    reverse_prev.next = prev_node

    return dummy.next
