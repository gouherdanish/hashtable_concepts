class HashTable:
    """
    Approach - Using two 1D arrays to track keys and values
    - Works on Linear Probing (a type of Open Addressing)
    - Resizes the table when load factor exceeds a limit
    
    """
    def __init__(self,capacity=2,load_factor_threshold=0.8) -> None:
        self._capacity = capacity
        self._size = 0
        self._lft = load_factor_threshold
        self._table = [[] for _ in range(self._capacity)]
    
    def __str__(self) -> str:
        res = ','.join([f'{k}:{v}' for bucket in self._table for k,v in bucket])
        return '{' + res + '}'
    
    def _resize(self,new_capacity):
        new_table = [[] for _ in range(new_capacity)]
        for bucket in self._table:
            for key, val in bucket:
                new_idx = hash(key) % new_capacity
                new_table[new_idx].append((key,val))
        self._table = new_table
        self._capacity = new_capacity

    def put(self,key,val):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = hash(key) % self._capacity
        if self._size * self._lft > self._capacity:
            self._resize(2*self._capacity)
        bucket = self._table[idx]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = val
                return
        self._table[idx].append((key,val))
        self._size += 1
    
    def get(self,key):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = hash(key) % self._capacity
        bucket = self._table[idx]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,val):
        self.put(key,val)
        
if __name__=='__main__':
    ht = HashTable()
    ht.put(1,4)
    print(ht)
    ht.put(11,5)
    print(ht)
    ht.put(2,3)
    print(ht)
    print(ht.get(11))
    print(ht.get(14))
    ht[5] = 3
    print(ht)
    print(ht[2])