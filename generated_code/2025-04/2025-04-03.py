class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one element, it is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using the slow and fast pointer technique
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None  # Break the list into two halves
        
        # Step 2: Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        
        # Merge the two lists in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach any remaining elements from either list
        current.next = l1 if l1
