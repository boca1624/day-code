class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    def merge_two_lists(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    if not lists:
        return None

    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            l1, l2 = lists[i], lists[i+1] if i+1 < len(lists) else None
            new_lists.append(merge_two_lists(l1, l2))
        lists = new_lists

    return lists[0]
