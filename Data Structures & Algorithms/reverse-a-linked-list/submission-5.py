# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        return prev

"""
prev = 3
cur = None
nextNode = None

       
None <- 0 <- 1 <- 2 <- 3 None

prev   cur   n
None <- 0 -> 1
       prev  cur  n
None <- 0 -> 1 -> 2


nextNode = cur.next
cur.next = prev
prev = cur
cur = nextNode

Complexity:
    - O(n) time since we traverse the list once
    - O(1) aux space and O(n) output space

"""