from collections.abc import Iterable


class Map:
    def __init__(self, func, *iterables):
        self._validate(func, iterables)
        self._func = func
        self._iterators = [iter(seq) for seq in iterables]

    def __iter__(self):
        return self
    
    def __next__(self):
        return self._func(*[next(it) for it in self._iterators])
    

    def _validate(self, func, iterables):
        if not callable(func):
            raise TypeError(f"'{func}' object is not callable")
        
        if not iterables:
            raise TypeError("Map() must have at least two arguments.")
        
        for iterable in iterables:
            if not isinstance(iterable, Iterable):
                raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    


def map_(func, *iterables):
    iterators = [iter(seq) for seq in iterables]

    while True:
        values = []
        for iterator in iterators:
            try:
                values.append(next(iterator))
            except StopIteration:
                return
        yield func(*values)




def test_map_1():
    colors = ['red', 'yellow', 'green']

    real_map = list(map(str.upper, colors))
    own_map = list(Map(str.upper, colors))

    assert real_map == own_map, "Test-1: Failed!"
    print("Test-1: Passed!")



def test_map_2():
    colors = ['red', 'yellow', 'green']
    numbers = [1, 2, 3, 4, 5]
    hello = "Hello"

    real_map = list(map(lambda *agrs: agrs, colors, numbers, hello))
    own_map = list(map_(lambda *agrs: agrs, colors, numbers, hello))

    assert real_map == own_map, "Test-2: Failed!"
    print("Test-2: Passed!")


if __name__ == "__main__":
    test_map_1()
    test_map_2()
