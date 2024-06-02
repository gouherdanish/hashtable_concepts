class HashTable:
    """
    Approach - Using two 1D arrays to track keys and values
    - Works on Linear Probing (a type of Open Addressing)

    Drawback
    - This insert implementation will run into infinite loop when the array gets full
    since it will keep on searching for an empty space (no vacant parking spot)
    - We can implement a resizing hashtable to avoid this
    
    """
    def __init__(self) -> None:
        self._capacity = 2
        self._keys = [None]*self._capacity
        self._vals = [None]*self._capacity
    
    def __str__(self) -> str:
        res = ','.join([f'{self._keys[i]}:{self._vals[i]}' for i in range(self._capacity) if self._keys[i] is not None])
        return '{' + res + '}'

    def put(self,key,val):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = hash(key) % self._capacity
        while self._keys[idx] is not None:
            if self._keys[idx] == key:
                self._vals[idx] = val
                return
            idx = (idx+1) % self._capacity
        self._keys[idx] = key
        self._vals[idx] = val
        
    def get(self,key):
        """
        Time - O(1) on average, O(n) in worst case
        """
        idx = hash(key) % self._capacity
        while self._keys[idx] is not None:
            if self._keys[idx] == key:
                return self._vals[idx]
            idx = (idx+1) % self._capacity
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
    

    
    