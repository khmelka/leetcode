from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    head = ListNode(0)
    current = head
    carry = 0

    while l1 or l2 :
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum = carry + x + y
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)
while result is not None:
    print(result.val, end=" -> " if result.next else "")
    result = result.next
print()
# 7 -> 0 -> 8
