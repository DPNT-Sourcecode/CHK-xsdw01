# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not isinstance(x, int) and isinstance(y, int):
        raise TypeError('Both inputs should be integers')
    if (x > 100) or (y > 100):
        raise ValueError('Both inputs should be 100 or less')
    if (x < 0) or (y < 0):
        raise ValueError('Both inputs should be positive integers')
    return x + y
