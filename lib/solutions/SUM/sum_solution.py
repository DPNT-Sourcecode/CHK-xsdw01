# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not isinstance(x, int) and isinstance(y, int):
        raise TypeError('Both inputs should be integers')
    return x + y
