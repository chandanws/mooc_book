
def flatten(nested):
    """
    When flatten is called, you have two possibilites: the base case and the recursive case.

    In the base case, the function is told to flatten a single element.
    In the recursive case, flatten it.

    >>> list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> list(flatten(['foo', ['bar', ['baz']]]))
    ['foo', 'bar', 'baz']
    """
    try:
        try:
            nested + ' '
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)