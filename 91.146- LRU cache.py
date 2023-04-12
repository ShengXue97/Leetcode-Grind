class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity= capacity
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # Insert node on right
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    # Remove node
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            self.remove(node)
        
        newNode = Node(key, value)
        self.insert(newNode)
        self.m[key] = newNode

        if len(self.m) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.m[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)