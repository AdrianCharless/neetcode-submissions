class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.dummyLeft = Node(0, 0)
        self.dummyRight = Node(0, 0)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): 
        last = self.dummyRight.prev
        last.next = node
        self.dummyRight.prev = node
        node.prev = last
        node.next = self.dummyRight


    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else:
            if len(self.keyMap) == self.capacity:
                last = self.dummyLeft.next
                self.remove(last)
                lastKey = last.key
                del self.keyMap[lastKey]
                node = Node(key, value)
                self.keyMap[key] = node
                self.insert(node)
            else:
                node = Node(key, value)
                self.insert(node)
                self.keyMap[key] = node
            
        
