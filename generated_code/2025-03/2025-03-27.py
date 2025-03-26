# 递归反转链表的代码示例

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    # 递归终止条件: 如果链表为空或只有一个节点
    if not head or not head.next:
        return head
    
    # 反转子链表
    reversed_head = reverse_linked_list(head.next)
    
    # 让当前节点成为子链表的最后一个节点
    head.next.next = head
    head.next = None
    
    return reversed_head

# 示例用法
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

reversed_head = reverse_linked_list(head)

# 输出反转后的链表
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
