class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to the node

        # dummy head and dummy tail for the doubly linked list
        self.left, self.right = Node(0, 0), Node(0, 0)  # left: LRU, right: most recent used

        # init the dummy node's relation
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # node: 1 <--> 2 <--> 3  ===>  1 <---> 3
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def insert(self, node):
        # right end (dummy tail) is the most recent used node --> insert into right end
        # 1<->2<->3 dt  ====> 1<->2<->3<->4 dt
        pre, nxt = self.right.prev, self.right
        pre.next = nxt.prev = node
        node.next, node.prev = nxt, pre  # 【※ 2-1】don't forget to link back into the DLL

    def get(self, key: int) -> int:
        if key in self.cache:
            # deal with the new action in the doubly linked list to track the LRC status
            # remove -> insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key in self.cache:
        #     cache[key] = Node(key, value)
        # cache[key] = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # deal with the cache pos for the cache[key] node
        # remove -> insert
        if len(self.cache) > self.cap:
            # evict LRU <=== Cache eviction policy
            # dh 1<->2<->3 dt
            LRU = self.left.next
            self.remove(LRU)
            # 【※ 2-1】don't forget to evict LRU from the cache
            del self.cache[LRU.key]


# # Cache eviction policy
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# # Data Structure
# hashmap
# double linked List
# two pointers: left-> lru; right-> most recent

# Time = O(1), Space = O(n), n = capacity
