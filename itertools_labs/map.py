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
    


def test_map_1():
    colors = ['red', 'yellow', 'green']

    real_map = list(map(str.upper, colors))
    own_map = list(Map(str.upper, colors))

    assert real_map == own_map, "Test-1: Failed!"
    print("Test-1: Passed!")




if __name__ == "__main__":
    test_map_1()