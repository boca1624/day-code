class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_k_sorted_lists(lists):
    if not lists:
        return None
    
    dummy = ListNode()
    current = dummy
    while True:
        min_node = None
        min_node_prev = None
        
        for i, l in enumerate(lists):
            if l:
                if min_node is None or l.value < min_node.value:
                    min_node = l
                    min_node_prev = i
        if min_node:
            current.next = min_node
            current = current.next
            lists[min_node_prev] = min_node.next
        else:
            break
            
    return dummy.next
