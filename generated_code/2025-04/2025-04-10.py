class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def rotate_linked_list(head, k):
    if not head or k == 0:
        return head

    # Step 1: Get the length of the list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Find the new head after rotation
    k = k % length  # Handle cases where k is greater than length
    if k == 0:
        return head

    # Step 3: Find the node before the new head
    current = head
    for _ in range(length - k - 1):
        current = current.next

    new_head = current.next
    current.next = None
    tail.next = head

    return new_head

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = rotate
