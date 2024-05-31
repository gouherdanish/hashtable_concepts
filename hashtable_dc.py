class Node:
    def __init__(self,key,val,next=None) -> None:
        self.key = key
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '->'.join([f'{node.key}:{node.val}' for node in self])
            
    def __iter__(self):
        curr = self
        while curr:
            yield curr
            curr = curr.next

class HashTable:
    """
    Approach - Using Linked List
    - Works on Direct Chaining

    Drawback
    """
    def __init__(self) -> None:
        self._capacity = 10
        self._data = [None]*self._capacity

    def __str__(self) -> str:
        res = ','.join([str(ll) for i, ll in enumerate(self._data) if ll])
        return '{' + res + '}'
    
    def _appendleft(self,sll,node):
        node.next = sll
        sll = node
        return sll

    def put(self,key,val):
        idx = key % self._capacity
        new_node = Node(key,val)
        sll = self._data[idx]
        print(sll)
        if sll is None:
            sll = new_node
        else:
            sll = self._appendleft(sll,new_node)
        print('After Append')
        print(sll)
        self._data[idx] = sll

    def _search(self,sll,key):
        while sll:
            if sll.key == key: return sll.val
            sll = sll.next
        return None

    def get(self,key):
        idx = key % self._capacity
        sll = self._data[idx]
        if sll is None: return None
        return self._search(sll,key)


if __name__=='__main__':
    ht = HashTable()
    ht.put(1,4)
    print(ht)
    ht.put(11,5)
    print(ht)
    ht.put(2,3)
    print(ht)
    print(ht.get(11))
    # sll = Node(1,11,Node(2,12))
    # print(sll)