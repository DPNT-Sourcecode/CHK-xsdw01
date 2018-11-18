

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """ This method returns:
            checkout(String) -> Integer
        Where:
            - param[0] = a String containing the SKUs of all the products
            in the basket
            - @return = an Integer representing the total checkout value
            of the items
    """

    if not isinstance(skus, basestring):
        return -1

    basket = {'a': 0,
              'b': 0,
              'c': 0,
              'd': 0}

    for sku in skus:
        if sku ==
