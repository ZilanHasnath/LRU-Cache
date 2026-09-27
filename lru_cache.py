class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node: Node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node

if __name__ == "__main__":
    cache = Cache(2)
    print("--- Initialized Cache with capacity 2 ---")
    cache.put("A", 10)
    print("put('A', 10)")
    cache.put("B", 20)
    print("put('B', 20)")
    print("get('A') returned:", cache.get("A"))
    cache.put("C", 30)
    print("put('C', 30) -> [Evicts 'B' because capacity is exceeded]")
    print("get('B') returned:", cache.get("B"))
    print("get('C') returned:", cache.get("C"))
    print("get('A') returned:", cache.get("A"))