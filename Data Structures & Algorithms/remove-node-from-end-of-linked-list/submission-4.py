# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = dummy
        p2 = dummy

        for index in range (n + 1):
            p2 = p2.next

        while p2:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return dummy.next


"""
dummy -> 1 -> 2 -> None
n = 2
        p1       
                    p2

n_front = sz - n
distance = p2 - p1 = n

when p2.next = None
p1 is at n + 1 from the end of the list
"""