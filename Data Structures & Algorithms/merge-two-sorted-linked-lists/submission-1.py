# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head = cur

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 if list1 else list2

        return head.next
"""
1 -> 2 -> 4
1 -> 3 -> 5




cur_node = ListNode()
cur_node_list1 = list1
cur_node_list2 = list2
head = cur_node
while cur_node_list1 or cur_node_list1 not null
    if cur_node_list1 is null:
        cur_node.next = cur_node_list2
        return head

    if cur_node_list1.val > cur_node_list2.val
        cur_node.val = list1.val
        cur_node_list1 = cur_node_list1.next
    else
        cur_node.val = list2.val
        cur_node_list2 = cur_node_list2.next

"""
        