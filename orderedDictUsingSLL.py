class SLLNode:
    def __init__(self,key=None,val=None) -> None:
        self.key = key
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f'{self.key}:{self.val}'

    def __repr__(self):
        return str(self)
    
class SLL:
    def __init__(self) -> None:
        self.head = SLLNode()
        self.size = 0
    
    def __iter__(self):
        curr = self.head.next
        while curr:
            yield (curr.key, curr.val)
            curr = curr.next

    def __str__(self) -> str:
        return '->'.join([str(node) for node in self])
    
    def __repr__(self):
        return str(self)
    
    def __bool__(self):
        return self.head.next is not None
    
    def __len__(self):
        return self.size
    
    def insert(self,key,val):
        curr = self.head
        while curr.next:
            if curr.next.key == key:
                curr.next.val = val
                self.size += 1
                return
            curr = curr.next
        new_node = SLLNode(key,val)
        curr.next = new_node
    
    def search(self,key):
        curr = self.head.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return None
    
    def delete(self,key):
        curr = self.head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    def items(self):
        curr = self.head.next
        while curr:
            yield (curr.key, curr.val)
            curr = curr.next
        

class OrderedDict:
    def __init__(self) -> None:
        self._capacity = 10
        self._table = [SLL() for _ in range(self._capacity)]
        self._global_list = SLL()

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

    def pop(self,key):
        idx = self._hash(key)
        self._table[idx].delete(key)
        self._global_list.delete(key)

    def items(self):
        yield from self._global_list


if __name__=='__main__':
    node = SLLNode(1,10)
    print(node)
    sll = SLL()
    sll.insert(1,10)
    sll.insert(2,20)
    print(sll)
    for item in sll.items():
        print(item)

    ht = OrderedDict()
    ht.put(1,10)
    print(ht)
    print(ht._table)
    ht.put(1,11)
    print(ht)
    print(ht._table)
    ht.put(2,20)
    print(ht)
    print(ht._table)
    ht.put(3,30)
    print(ht)
    print(ht._table)
    ht.put(11,110)
    print(ht)
    print(ht._table)
    print(ht.get(1))
    for item in ht.items(): 
        print(item)

    ht = OrderedDict()
    ht.put('apple',100)
    ht.put('banana',30)
    print(ht)
    ht.put('banana',50)
    print(ht)
    ht.pop('banana')
    print(ht)