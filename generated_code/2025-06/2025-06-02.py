class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_every_k_nodes(head: ListNode, k: int) -> ListNode:
    def reverse_segment(start: ListNode, end: ListNode) -> ListNode:
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # New head of the reversed segment

    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        group_next = kth.next
        # Reverse current k-group
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
