class Node:
    def __init__(self,key=None,val=None) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Node({self.key}:{self.val})'
    
    def __repr__(self) -> str:
        return str(self)

class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
        
    def __str__(self) -> str:
        return '<->'.join([str(node) for node in self])
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self):
        return self.size

    def insert(self,node):
        "Inserts at the end"
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

class OrderedDict:
    def __init__(self) -> None:
        self._capacity = 10
        self.dll = DLL()
        self.map = {}

    def __iter__(self):
        for node in self.dll:
            yield (node.key, node.val)

    def __str__(self) -> str:
        res = ', '.join([f'{k}:{v}' for k, v in self])
        return '{' + res + '}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self):
        return len(self.dll)

    def _hash(self,key):
        return hash(key) % self._capacity

    def put(self,key,val):
        if key in self.map:
            node = self.map[key]
            node.val = val
        else:
            new_node = Node(key,val)
            self.dll.insert(new_node)
            self.map[key] = new_node
    
    def get(self,key):
        if key in self.map:
            node = self.map[key]
            return node.val
        return None

if __name__=='__main__':
    od = OrderedDict()
    od.put(1,10)
    print(od)
    print(od.dll)
    od.put(1,11)
    print(od)
    print(od.dll)
    od.put(11,110)
    print(od)
    print(od.dll)
    od.put(2,20)
    print(od)
    print(od.dll)
    print(len(od))