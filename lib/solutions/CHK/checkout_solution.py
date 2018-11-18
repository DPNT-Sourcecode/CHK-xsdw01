

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
        a_deals = 0
        b_deals = 0
        e_deals = 0
        multi_a_deals = 0
        f_deals = 0

        if basket['A'] < 5:
            a_deals = basket['A'] / 3
        else:
            multi_a_deals = basket['A'] / 5
            a_deals = (basket['A'] - 5 * multi_a_deals) / 3
        if basket['E'] >= 2 and basket["B"] >= 1:
            e_deals = basket['E'] / 2
            if e_deals > basket['B']:
                e_deals = basket['B']
        b_deals = (basket['B'] - e_deals) / 2
        deals = {'A': a_deals,
                 'B': b_deals,
                 'E': e_deals,
                 'AAAAA': multi_a_deals}
        return deals

    if not isinstance(skus, basestring):
        return -1

    basket = {'A': 0,
              'B': 0,
              'C': 0,
              'D': 0,
              'E': 0}  # Currently case sensitive...

    for sku in skus:
        if sku in basket:
            basket[sku] += 1
        else:
            return -1

    deals = _check_for_deals(basket)

    """ This sum could be shortened, but I will leave it long for now
        to see what is going on """
    cost = (deals['A'] * 130 + deals['B'] * 45 + deals['AAAAA'] * 200 +
            (basket['A'] - 3 * deals['A'] - 5 * deals['AAAAA']) * 50 +
            (basket['B'] - 2 * deals['B'] - deals['E']) * 30 +
            basket['C'] * 20 +
            basket['D'] * 15 +
            basket['E'] * 40)
    return cost
