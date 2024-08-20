"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # make a dummy node, set current equal to dummy
    dummy = ListNode()
    current = dummy

    # while the lists aren't empty
    while list1 and list2:
        # if list1's val is less than list2's val
        if list1.val < list2.val:
            # set current's next to list1
            current.next = list1
            # set list1 to list1.next (incremnet along the list)
            list1 = list1.next
        # else
        else: 
            # set curr's next to list2
            current.next = list2
            # increment along list2
            list2 = list2.next
        # set current to current.next (increment along the list)

    # at the end of while loop, if there are still nodes in either list,
    # set that to the curr's next
    current.next = list1 if list1 else list2

    # return the dummy's next
    return dummy.next
    


print(merge_two_lists([1,2,4], [1,3,4])) # [1, 1, 2, 3, 4, 4]
print(merge_two_lists([], [])) # []
print(merge_two_lists([], [0])) # [0]
