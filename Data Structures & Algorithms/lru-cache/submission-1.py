class Node():
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.hash_storage = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.hash_storage:
            node = self.hash_storage[key]
            self.detach_from_list(node)
            self.add_to_head(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_storage:
            node = self.hash_storage[key]
            node.val = value
            self.get(key)
            return
        
        node = Node(key, value)
        if self.capacity == self.current_size:
            # remove LRU element
            lru_node = self.remove_from_tail()
            self.hash_storage.pop(lru_node.key)
        else:
            self.current_size += 1

        # add element after head
        self.hash_storage[key] = node
        self.add_to_head(node)

    def add_to_head(self, node: Node) -> None:
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node


    def remove_from_tail(self) -> Node:
        node = self.tail.prev
        prev_node = node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node

        return node


    def detach_from_list(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
"""
head <-> 4 <-> 3 <-> 2 <-> 1 <-> tail

add element when capacity is not full
    insert element to head of list
add element when capacity is full
    insert eleement after head and delete element before tail

get element from list
    move element from its current position to after head
"""