from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    start_point = ListNode(-1000)
    dummy_point = ListNode(-1000)
    start_point.next = dummy_point

    pointer_1 = list1
    pointer_2 = list2

    while(pointer_1 and pointer_2):
        if(pointer_1.val < pointer_2.val):
            dummy_point.next = pointer_1
            pointer_1 = pointer_1.next
        else:
            dummy_point.next = pointer_2
            pointer_2 = pointer_2.next
        dummy_point  = dummy_point.next

    if(pointer_1 and not pointer_2):
        dummy_point.next = pointer_1
        
    if(not pointer_1 and pointer_2):
        dummy_point.next = pointer_2
        
    return start_point.next.next