# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_middle(self, head: Optional[ListNode]):
        # finding the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        return head2

    def reverse_list(self, head2: Optional[ListNode]):
        # reverse 2nd half. prev is now head of reversed list
        prev = None
        while head2:
            next_node = head2.next
            head2.next = prev
            prev = head2
            head2 = next_node

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        head2 = self.find_middle(head)
        head2_reverse = self.reverse_list(head2)

        # reorder the list
        c1 = head
        c2 = head2_reverse
        while c2:
            next1 = c1.next
            next2 = c2.next
            c1.next = c2
            c2.next = next1
            c1 = next1
            c2 = next2

            



"""
Finding the middle
2 -> 4 -> 6 -> 8
     s         f

2 -> 4 -> 6 -> 8 -> 10
          s    
                    f

2 -> 4 -> None
8 -> 6 -> None

2 -> 4 -> 6 -> None
10 -> 8 -> None



"""