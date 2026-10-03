class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This key was just used, so move it to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)
        self.cache[key] = node

        # New/updated key becomes MRU
        self.insert(node)
        
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, node):
        # Insert just before right (MRU position)
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node
        # Too many items
        if len(self.cache) > self.capacity:

            # LRU node is right after left dummy
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]