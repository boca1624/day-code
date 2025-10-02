class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    prev = head
    while prev != slow:
        prev = prev.next
        slow = slow.next
    return prev

def merge_k_sorted_lists(lists):
    dummy = ListNode()
    tail = dummy
    while lists:
        min_head = None
        for i, lst in enumerate(lists):
            if lst:
                if min_head is None or lst.val < min_head.val:
                    min_head = lst
        if min_head:
            tail.next = min_head
            tail = min_head
            lists[lists.index(min_head)] = min_head.next
    return dummy.next

def partition(head, x):
    before_head = before = ListNode(0)
    after_head = after = ListNode(0)
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next
