#68ms

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    n1 = ""
    n2 = ""
    while l1:
        n1 = str(l1.val) + n1
        l1 = l1.next
    while l2:
        n2 = str(l2.val) + n2
        l2 = l2.next
    s = str(int(n1) + int(n2))
    head = ListNode()
    ln = head
    for i in range(len(s) - 1, -1, -1):
        ln.val = int(s[i])
        if i != 0:
            ln.next = ListNode()
            ln = ln.next
    return head
