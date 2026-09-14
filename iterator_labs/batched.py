

class Batched:
    def __init__(self, iterable, n: int, *, strict=False):
        self._iterator = iter(iterable)
        self._n = n
        self._strict = strict

    def __iter__(self):
        return self
    
    def __next__(self):
        values = []
        for _ in range(self._n):
            try:
                values.append(next(self._iterator))
            except StopIteration:
                if not values:
                    raise StopIteration
                elif self._strict:
                    raise ValueError
                break
        return tuple(values)
    
