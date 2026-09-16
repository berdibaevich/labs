

def chain_(*iterables):
    for iterable in iterables:
        yield from iterable