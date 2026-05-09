"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_hash = {}
        dummy = Node(0)

        cur = head
        while cur:
            node_hash[cur] = Node(cur.val)
            cur = cur.next
        node_hash[None] = None

        cur = head
        dummy.next = node_hash[cur]
        while cur:
            new_node = node_hash[cur]
            new_node.next = node_hash[cur.next]
            new_node.random = node_hash[cur.random]
            cur = cur.next

        return dummy.next
            

        

"""
None 3    0    1
^    ^
|    |
3 -> 7 -> 4 -> 5 -> None

dict = {
    3 : 3


}





"""
        