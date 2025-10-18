class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_k_group(head, k):
    if not head or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    current = head

    while True:
        count = 0
        group_next = None
        while current and count < k:
            group_next = current.next
            current.next = group_prev.next
            group_prev.next = current
            current = group_next
            count += 1

        group_prev = head
        head = group_next

        if count != k:
            break

    return dummy.next
