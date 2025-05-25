from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:

        dummy  = ListNode(0, head)
        prev_node = dummy
        current_node = head
        while(current_node and current_node.next):
            # Save values
            next_node_2 = current_node.next.next
            next_node = current_node.next
            # Modify pointers
            current_node.next = next_node.next
            next_node.next = current_node
            prev_node.next = next_node

            # Update pointers
            prev_node = current_node
            current_node = next_node_2

        return dummy.next


def main():
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    a = swapPairs(node1)

    print(a)

if __name__=='__main__':
    main()