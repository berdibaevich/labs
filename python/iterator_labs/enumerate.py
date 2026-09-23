

class Enumerate:
    def __init__(self, iterable, start=0):
        self._iterator = iter(iterable)
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        self._start += 1
        return self._start - 1, next(self._iterator)



def enumerate_(iterable, start=0):
    for seq in iterable:
        yield start, seq
        start += 1


