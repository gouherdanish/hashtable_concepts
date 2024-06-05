class HashSet:
    """
    Using an array of Singly Linked List
    """
    def __init__(self) -> None:
        self._capacity = 10
        self._buckets = [[] for _ in range(self._capacity)]

    def __str__(self) -> str:
        res = ', '.join([str(x) for bucket in self._buckets for x in bucket])
        return '{' + res + '}'
    
    def __len__(self):
        return sum(len(bucket) for bucket in self._buckets)

    def _hash(self,key):
        return hash(key) % self._capacity

    def add(self,key):
        idx = self._hash(key)
        if key not in self._buckets[idx]:
            self._buckets[idx].append(key)
    
    def contains(self,key):
        return self.__contains__(key)

    def __contains__(self,key):
        idx = self._hash(key)
        return key in self._buckets[idx]
    
    def pop(self,key):
        idx = self._hash(key)
        if key in self._buckets[idx]:
            self._buckets[idx].remove(key)


if __name__=='__main__':
    s = HashSet()
    s.add(1)
    print(len(s))
    s.add(1)
    print(s)
    print(len(s))
    s.add(11)
    print(s)
    print(len(s))
    s.add(2)
    print(s)
    print(len(s))
    print(s)
    print(11 in s)
    s.pop(11)
    print(s)