class DllNode:
    def __init__(self, key=None, val=None, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f'{self.key}:{self.val}'

class DLL:
    """
    Using DLL to store the 
    """
    def __init__(self) -> None:
        self.head = DllNode()
        self.tail = DllNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __iter__(self):
        curr = self.head.next
        while curr.next:
            yield curr
            curr = curr.next

    def __str__(self) -> str:
        return '<->'.join([str(node) for node in self]) if self.head else ''
    
    def insert(self,key,val):
        # If key exists, then update
        curr = self.head.next
        while curr != self.tail:
            if curr.key == key:
                curr.val = val
                return
            curr = curr.next
        # Else insert at the end
        new_node = DllNode(key,val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def search(self,key):
        # if key exists, return val 
        curr = self.head.next
        while curr != self.tail:
            if curr.key == key:
                return curr.val
            curr = curr.next
        # if not found, then return None
        return None
    
    def items(self):
        curr = self.head.next
        while curr.next:
            yield (curr.key,curr.val)
            curr = curr.next

class OrderedDict:
    def __init__(self) -> None:
        self._capacity = 10
        self._table = [DLL() for _ in range(self._capacity)]
        self._global_list = DLL()

    def __str__(self) -> str:
        res = ', '.join([f'{k}:{v}' for k,v in self.items()])
        return '{' + res + '}'

    def _hash(self,key):
        return hash(key) % self._capacity
    
    def put(self,key,val):
        idx = self._hash(key)
        self._table[idx].insert(key,val)
        self._global_list.insert(key,val)
    
    def get(self,key):
        idx = self._hash(key)
        return self._table[idx].search(key)
    
    def items(self):
        return self._global_list.items()
    

if __name__=='__main__':
    node = DllNode(1,10)
    print(node)
    dll = DLL()
    dll.insert(1,10)
    dll.insert(2,20)
    print(dll)
    ht = OrderedDict()
    ht.put(1,4)
    print(ht)
    ht.put(1,5)
    print(ht)
    ht.put(2,3)
    print(ht)
    ht.put(11,5)
    print(ht)
    print(ht.get(1))
    for item in ht.items(): 
        print(item)

    ht = OrderedDict()
    ht.put('apple',100)
    ht.put('banana',30)
    print(ht)