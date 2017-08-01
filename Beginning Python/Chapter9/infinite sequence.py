def checkIndex(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start   - the first value in the sequence
        step    - the difference between two adjacent values
        changed - a dictionary of values that have been modified by the user
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step
    # Store the start value
    # Store the step value
    # No items have been modified
    # Modified?
    # otherwise...
    # ...calculate the value

    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """
        checkIndex(key)
        self.changed[key] = value                 # Store the changed value

    def __delitem__(self, key):
        """
        Delete the key provided from sequence
        """
        checkIndex(key)
        del self.changed[key]



if __name__ == "__main__":
    s = ArithmeticSequence(1, 2)
    print(s[4])
    s[4]=3
    print(s[4])
    del s[4]
    print(s[4])
