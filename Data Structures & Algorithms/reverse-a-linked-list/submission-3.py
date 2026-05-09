# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return null or single node list
        if not head or not head.next:
            return head

        # recursive case
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head




"""
0 -> 1 -> null

1st stack





"""