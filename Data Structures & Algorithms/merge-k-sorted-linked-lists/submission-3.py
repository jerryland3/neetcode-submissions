# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        i = 0
        for head in lists:
            if head:
                listTuple = (head.val, i, head)
                minHeap.append(listTuple)
                i += 1
        heapq.heapify(minHeap)

        dummy = ListNode()
        cur = dummy
        while minHeap:
            _, _, smallestNode = heapq.heappop(minHeap)
            smallestNext = smallestNode.next
            cur.next = smallestNode
            cur = cur.next
            if smallestNext:
                heapq.heappush(minHeap, (smallestNext.val, i, smallestNext))
                i += 1
        
        return dummy.next
            

"""
1  2  4
1  2  5
3  6 

smallest = (2, 4, 2)
smallestNext = 4
dummy -> 1 -> 1 -> 2 -> 2 -> 4 ... -> 6

Strategy:
    [c1 c2 c3 ... ck]
    - build a heap with the k cur nodes from the k list
    - pop the smallest and point current output node at that node
    - get the next node for that smallest node if it exist, and push into the heap
    - keep doing this until the heap is empty (while loop)

Heap Structure:
    - python heap does not compare the object (raise TypeError), use the value of the node as comparison
      i.e. (node.val, i, node). The i is a unique index to prevent comparison error if two node.val are the same.
      i is incremented every loop.

Edge Cases:
    - using a sentinel node for the head node will make logic easier, less edge case check for the first node.

Complexity:
    - Need to step through every node in the lists, n steps. At each step, need to push into the heap, log(k).
      Building the heap is O(k) time and is only done once, does not contribute to total time complexity. Thus,
      Overall time complexity is O(n*log(k))
    - Space complexity of O(k) for the heap, and O(n) output space.
"""
        