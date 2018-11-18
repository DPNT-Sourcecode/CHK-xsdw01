

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

    def _multibuy(item, discount):
        return = items / discount

    def _double_multibuy(item, discount_low, discount_high):
        num_deals_high = item / discount_high
        num_deals_low = (item - discount_high*num_deals_high) / discount_low
        return (num_deals_high, num_deals_low)

    def _bogof(items, discounted_items, threshold):
        if items >= threshold and discounted_items >= 1:
            num_deals = items / threshold
            if num_deals > discounted_items:
                num_deals = discounted_items
        return num_deals

    def _check_off_items_in_deal(rem_basket, item_key, num_items):
        rem_basket[item_key] = rem_basket[item_key] - num_items
        if rem_basket[item_key] < 0:
            print "Have removed more items from deals than existed"
            raise ValueError
        return rem_basket

    def _check_for_deals(basket):
        remaining_basket = basket.copy()
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

        f_deals = basket['F'] / 3  # Equivalent to 2 + 1
        deals = {'A': a_deals,
                 'B': b_deals,
                 'E': e_deals,
                 'F': f_deals,
                 'AAAAA': multi_a_deals}
        return deals

    if not isinstance(skus, basestring):
        return -1

    basket = dict()
    import string
    for letter in string.ascii_uppercase:
        basket[letter] = 0
    # basket = {'A': 0,
    #           'B': 0,
    #           'C': 0,
    #           'D': 0,
    #           'E': 0,
    #           'F': 0}  # Currently case sensitive...

    for sku in skus:
        if sku in basket:
            basket[sku] += 1
        else:
            return -1

    deals = _check_for_deals(basket)

    """ This sum could be shortened, but I will leave it long for now
        to see what is going on """
    cost = (deals['A'] * 130 + deals['B'] * 45 +
            deals['AAAAA'] * 200 + deals['F'] * 20 +
            (basket['A'] - 3 * deals['A'] - 5 * deals['AAAAA']) * 50 +
            (basket['B'] - 2 * deals['B'] - deals['E']) * 30 +
            basket['C'] * 20 +
            basket['D'] * 15 +
            basket['E'] * 40 +
            (basket['F'] - 3 * deals['F']) * 10)
    return cost
