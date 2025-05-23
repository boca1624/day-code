class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a portion of the list
        def reverse_linked_list(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth_node = group_prev
            # Find the k-th node from the current position
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            
            group_next = kth_node.next
            # Reverse the k-group
            group_start = group_prev.next
            group_end = kth_node.next
            kth_node.next = None
            group_prev.next = reverse_linked_list(group_start, group_end)
            group_start.next = group_next
            group_prev = group_start
        
        return dummy.next
