class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a segment of the list
        def reverse_segment(head, k):
            prev, curr = None, head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        # Initialize a dummy node and a pointer to handle the head of the list
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while head:
            # Check if there are enough nodes to reverse
            tail = group_prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            
            group_next = tail.next
            group_start = group_prev.next
            group_prev.next = reverse_segment(group_start, k)
            group_start.next = group_next
            group_prev = group_start
            head = group_next
            
        return dummy.next
