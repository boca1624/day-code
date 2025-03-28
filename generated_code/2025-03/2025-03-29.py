class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse_k_group(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while head:
            group_start = head
            group_end = head
            for i in range(k-1):
                group_end = group_end.next
                if not group_end:
                    return dummy.next
            
            next_group_start = group_end.next
            group_end.next = None

            prev, curr = None, group_start
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            prev_group_end.next = prev
            group_start.next = next_group_start
            prev_group_end = group_start
            head = next_group_start
        
        return dummy.next

    def print_list(self):
        current = self.head
        while
