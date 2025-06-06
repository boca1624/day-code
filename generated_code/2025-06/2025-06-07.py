class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode) -> None:
    """
    Reorder a linked list in the following pattern:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    The function modifies the list in-place.
    """
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev, curr = None, slow.next
    slow.next = None  # Split the list into two
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # Step 3: Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
