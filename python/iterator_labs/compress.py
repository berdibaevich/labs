

class Compress:
    def __init__(self, data, selectors):
        self._data = iter(data)
        self._selectors = iter(selectors)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self._data)
            selector = next(self._selectors)
            
            if selector:
                return value
            


def compress_(data, selectors):
    yield from (v for v, f in zip(data, selectors) if f)
