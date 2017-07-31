import random


class UniversalHash:
    """
    >>> h=UniversalHash()
    >>> h[54]="cat"
    >>> h[26]="dog"
    >>> h[93]="lion"
    >>> h[77]="bird"
    >>> h[31]="cow"
    >>> h[44]="goat"
    >>> 54 in h
    True
    """
    def __init__(self):
        (self.p, self.a, self.b) = self.generate_hash_constants()
        self.size = self.p
        self.slots = [None] * self.size
        self.data = [None]* self.size

    def generate_hash_constants(self):
        """
        generate a, b, p for universal hashing
        """
        p = self._get_prime()  # set p a  random prime number
        a = random.randint(1, p - 1)  # A has a random value between 1 and p - 1.
        b = random.randint(1, p - 1)  # B has a random value between 1 and p - 1
        return p, a, b

    def put(self, key, data):
        hash_value = self.hash_function(key)
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

    def hash_function(self, key):
        """
        hash_function implements the simple remainder method
        """
        return round(self.a * key + self.b) % self.p

    def rehash(self, old_hash, size):
        """
        linear probing with a plus 1
        """
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key)
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

    def _is_prime(self,n):
        if n <= 2 or n%2 == 0:
            return False

        return not any((n%i == 0 for i in range(3, n-1)))

    def _get_prime(self, p=0):
        """
        get a prime number
        """
        if p == 0:
            p = random.randint(1000000,10000000)
        while not self._is_prime(p):
            p += 1

        return p

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