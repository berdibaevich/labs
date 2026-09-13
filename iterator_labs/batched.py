

class Batched:
    def __init__(self, iterable, n: int):
        self._iterator = iter(iterable)
        self._n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        values = []
        for _ in range(self._n):
            try:
                values.append(next(self._iterator))
            except StopIteration:
                if values:
                    break
                raise StopIteration
        return tuple(values)
    
