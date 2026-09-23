

class Count:
    def __init__(self, start=0, step=1):
        self._current = start
        self._step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        val = self._current
        self._current += self._step
        return val
    


def count_(start=0, step=1):
    while True:
        yield start
        start += step 