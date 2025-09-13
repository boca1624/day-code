class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_k_group(head, k):
    if not head or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    count = 0

    while curr:
        count += 1
        if count == k:
            prev.next, curr.next, prev = curr.next, prev, curr
            count = 0
        curr = curr.next

    return dummy.next
