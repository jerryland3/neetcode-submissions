# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        prev_node = head
        cur_node = head.next
        next_node = cur_node.next
    
        while next_node != None :
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.next

        cur_node.next = prev_node
        head.next = None
        return cur_node








"""
0 -> 1 -> 2 -> 3 -> null





"""