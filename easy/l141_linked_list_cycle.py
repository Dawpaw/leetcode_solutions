from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next:ListNode | None= next


def hasCycle(head: Optional[ListNode]) -> bool:
    current = head
    cycle = False
    if not current or not current.next:
        return False
    fast = current.next.next
    while(fast):
        if(not fast.next):
            break
        if(fast.next == current):
            cycle = True
            break
        current = current.next
        fast = fast.next.next
    return cycle

def has_cycle_solution(head: ListNode) -> bool:
        # Initialize two pointers, slow and fast. Both start at the head of the list.
        slow_pointer = fast_pointer = head
        # Loop until fast_pointer reaches the end of the list
        while fast_pointer and fast_pointer.next:
            # Move slow_pointer by one step
            slow_pointer = slow_pointer.next
            # Move fast_pointer by two steps
            fast_pointer = fast_pointer.next.next
            # If slow_pointer and fast_pointer meet, there's a cycle
            if slow_pointer == fast_pointer:
                return True
        # If fast_pointer reaches the end, there is no cycle
        return False

i = 0
d = ListNode(-4)
i += 1
c = ListNode(0, d)
i += 1
b = ListNode(2, c)
i += 1
a = ListNode(3, b)

d.next = b

hasCycle(a)

