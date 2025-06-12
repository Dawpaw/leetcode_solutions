# https://leetcode.com/problems/reverse-linked-list/description/?envType=problem-list-v2&envId=recursion

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(vals:list[int]):
    nodes  = []
    for val in vals:
        nodes.append(ListNode(val))

    for i in range(len(nodes)-1):
        nodes[i].next =  nodes[i+1]

    return nodes[0]


def reverseList(head):
    # Base case
    if (head is None or head.next is None):
        return head

    # Flip
    next = reverseList(head.next)
    head.next.next = head
    head.next = None
    return next


head = [1,2,3,4,5]

linked_list = create_linked_list(head)
a = reverseList(linked_list)
print(a)