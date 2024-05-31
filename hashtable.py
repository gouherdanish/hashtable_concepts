class HashTable:
    """
    Approach - Using Array

    Drawback
    - Collision happens between same hashed keys after capacity is exceeded
    """
    def __init__(self) -> None:
        self._capacity = 1000
        self._data = [None]*self._capacity

    def __str__(self) -> str:
        res = ', '.join([f'{i}:{x}' for i, x in enumerate(self._data) if x])
        return '{'+res+'}'

    def _hash(self, key):
        return key % self._capacity

    def put(self,key,val):
        idx = self._hash(key)
        self._data[idx] = val

    def get(self,key):
        idx = self._hash(key)
        return self._data[idx]
    
    def pop(self,key):
        idx = self._hash(key)
        self._data[idx] = None
    
if __name__=='__main__':
    ht = HashTable()
    ht.put(1,4)
    print(ht.get(2))
    print(ht)
    ht.put(1,3)
    print(ht)
    ht.put(1001,300)
    print(ht)
    ht.pop(1)
    print(ht)