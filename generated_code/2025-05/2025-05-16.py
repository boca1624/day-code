# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转链表的部分区域 [m, n]，1 ≤ m ≤ n ≤ 链表长度
def reverse_between(head, m, n):
    if not head or m == n:
        return head

    # 创建虚拟头节点，简化边界处理
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    # 找到反转区域前的节点
    for _ in range(m - 1):
        pre = pre.next

    # 开始反转区域
    reverse = None
    cur = pre.next
    for _ in range(n - m + 1):
        next_node = cur.next
        cur.next = reverse
        reverse = cur
        cur = next_node

    # 连接反转区域和剩余链表
    pre.next.next = cur
    pre.next = reverse

    return dummy.next

# 创建链表示例：1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# 反转链表部分区域 [2, 4]：1 ->
