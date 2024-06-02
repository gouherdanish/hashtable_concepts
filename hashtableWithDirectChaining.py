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
        res = ','.join([str(node) for i, node in enumerate(self._data) if node])
        return '{' + res + '}'

    def put(self,key,val):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = key % self._capacity
        if self._data[idx] is None:
            self._data[idx] = Node(key,val)
        else:
            curr = self._data[idx]
            while curr.next:
                if curr.key == key:
                    curr.val = val
                    return
                curr = curr.next
            curr.next = Node(key,val)

    def get(self,key):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = key % self._capacity
        curr = self._data[idx]
        while curr:
            if curr.key == key: 
                return curr.val
            curr = curr.next
        return None

if __name__=='__main__':
    ht = HashTable()
    ht.put(1,4)
    print(ht)
    ht.put(1,5)
    print(ht)
    ht.put(11,5)
    print(ht)
    ht.put(2,3)
    print(ht)
    print(ht.get(11))
    # sll = Node(1,11,Node(2,12))
    # print(sll)