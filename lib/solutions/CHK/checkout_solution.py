

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


    def _check_for_deals(basket):
        a_deals = int(round(basket['a'] / 3))
        b_deals = int(round(basket['b'] / 2))
        deals = {'a': a_deals,
                 'b': b_deals}  # Might be useful to have this separate
        return deals

    if not isinstance(skus, basestring):
        return -1

    basket = {'A': 0,
              'B': 0,
              'C': 0,
              'D': 0}  # Currently case sensitive...

    for sku in skus:
        if sku in basket:
            basket[sku] += 1
        else:
            return -1

    deals = _check_for_deals(basket)
    cost = (deals['a'] * 130 + deals['b'] * 45 +
            (basket['a'] - 3) * 50 +
            (basket['b'] - 2) * 30 +
            basket['c'] * 20 +
            basket['d'] * 15)
    return cost
