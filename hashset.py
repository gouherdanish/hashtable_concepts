class SllNode:
    def __init__(self,key=None) -> None:
        self.key = key
        self.next = None

    def __str__(self) -> str:
        return f'{self.key}'
    
class SLL:
    def __init__(self) -> None:
        self.head = SllNode()
        self.size = 0

    def __iter__(self):
        curr = self.head.next
        while curr:
            yield curr
            curr = curr.next

    def __str__(self) -> str:
        res = ', '.join([str(node) for node in self])
        return res
    
    def __bool__(self):
        return self.head.next is not None
    
    def __len__(self):
        return self.size

    def insert(self,key):
        curr = self.head
        while curr.next:
            if curr.key == key:
                return
            curr = curr.next
        curr.next = SllNode(key)
        self.size += 1

    def search(self,key):
        curr = self.head
        while curr.next:
            if curr.key == key:
                return True
            curr = curr.next
        return False
    
    def delete(self,key):
        curr = self.head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next
        
class HashSet:
    def __init__(self) -> None:
        self._capacity = 10
        self._table = [SLL() for _ in range(self._capacity)]

    def __str__(self) -> str:
        res = ', '.join([str(bucket) for bucket in self._table if bucket])
        return '{' + res + '}'
    
    def __len__(self):
        return sum(len(bucket) for bucket in self._table if bucket)

    def _hash(self,key):
        return hash(key) % self._capacity

    def add(self, key):
        idx = self._hash(key)
        self._table[idx].insert(key)
    
    def __contains__(self,key):
        idx = self._hash(key)
        return self._table[idx].search(key)
    
    def pop(self,key):
        idx = self._hash(key)
        self._table[idx].delete(key)

if __name__=='__main__':
    s = HashSet()
    s.add(1)
    print(len(s))
    s.add(11)
    print(s)
    print(len(s))
    s.add(2)
    print(s)
    print(len(s))


