

class Chain:
    def __init__(self, *iterables):
        self._iterables = iterables
        self._index = 0
        self._current_iter = None
        self._length = len(self._iterables)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self._current_iter is None:
                self._current_iter = iter(self._iterables[self._index])
            try:
                return next(self._current_iter)
            except StopIteration:
                if (index := self._index + 1) < self._length:
                    self._current_iter = None
                    self._index = index
                    continue
                raise 


def chain_(*iterables):
    for iterable in iterables:
        yield from iterable