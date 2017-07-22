
class HashTable:
    """
    >>> h=HashTable()
    >>> h[54]="cat"
    >>> h[26]="dog"
    >>> h[93]="lion"
    >>> h[77]="bird"
    >>> h[31]="cow"
    >>> h[44]="goat"
    >>> h.slots
    [77, 44, None, None, 26, 93, None, None, None, 31, 54]
    >>> h.data
    ['goat', None, None, None, 'dog', 'lion', None, None, None, 'cow', 'cat']
    >>> 54 in h
    True
    """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None]* self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            # rehash
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = self.rehash(hash_value, len(self.slots))

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[hash_value] = data
            else:
                self.data[hash_value] = data

    def hash_function(self, key, size):
        """
        hash_function implements the simple remainder method
        """
        return key % size

    def rehash(self, old_hash, size):
        """
        linear probing with a plus 1
        """
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
            if position == start_slot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        """
        return length
        """
        count = 0
        for item in self.slots:
            if item is not None:
                count += 1

        return count

    def __contains__(self, item):
        """
        定义了使用in和not in进行成员测试时类的行为
        """
        return self.get(item) is not None


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)