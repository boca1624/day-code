class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_second_largest_node(head):
    if not head or not head.next:
        return None
    
    prev, curr, second_largest = None, head, head.next
    
    while curr:
        if curr.val > second_largest.val:
            prev = second_largest
            second_largest = curr
        elif curr.val < second_largest.val and (prev is None or curr.val > prev.val):
            prev = second_largest
            second_largest = curr
        
        curr = curr.next
    
    return second_largest if prev is not None else None
