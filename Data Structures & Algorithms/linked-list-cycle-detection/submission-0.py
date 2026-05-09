# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()

        while head:
            if head in hashset:
                return True
            
            hashset.add(head)
            head = head.next
        
        return False

"""
1 2

hashset = [1 2]

head = None


use hash to keep track of nodes

traverse the list
    if we see a node already in hash set return true
    if we see the next pointer is null return false
"""
        