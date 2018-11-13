# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Both inputs should be integers')
