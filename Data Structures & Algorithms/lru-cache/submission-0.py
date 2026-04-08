class CacheNode:
    def __init__(self, key: int, value: init) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = CacheNode(0,0)
        self.tail = CacheNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # Remove node from linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        # Add node right after head (MRU position)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add_to_front(node)
        else:
            node = CacheNode(key,value)
            self.cache[key] = node
            self.add_to_front(node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self.remove(lru_node)
                del self.cache[lru_node.key]
            

