

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

    def _multibuy(items, discount):
        num_deals = items /discount
        return (num_deals, items - (num_deals * discount))

    def _double_multibuy(items, discount_low, discount_high):
        num_deals_high = items / discount_high
        remaining = items - discount_high * num_deals_high
        num_deals_low = remaining / discount_low
        remaining = items - discount_low * num_deals_low
        return (num_deals_high, num_deals_low, remaining)

    def _bogof(items, discounted_items, threshold):
        if items >= threshold and discounted_items >= 1:
            num_deals = items / threshold
            if num_deals > discounted_items:
                num_deals = discounted_items
        remaining_items = items - num_deals * threshold
        remaining_discounted_items = discounted_items - num_deals
        return (num_deals, remaining_items, remaining_discounted_items)

    def _check_off_items_in_deal(rem_basket, item_key, num_items):
        rem_basket[item_key] = rem_basket[item_key] - num_items
        if rem_basket[item_key] < 0:
            print "Have removed more items from deals than existed"
            raise ValueError
        return rem_basket

    def _check_for_deals(basket):
        remaining_basket = basket.copy()
        deals = dict()

        deals['5A'], deals['3A'],
        remaining_basket = _double_multibuy(remaining_basket['A'], 3, 5)

        remaining_basket['A'] -= 3*deals['3A']
        remaining_basket['A'] -= 5*deals['5A']

        deals['2B'] = _multibuy(remaining_basket['B'])
        print deals['B']

        # if basket['A'] < 5:
        #     a_deals = basket['A'] / 3
        # else:
        #     multi_a_deals = basket['A'] / 5
        #     a_deals = (basket['A'] - 5 * multi_a_deals) / 3
        #
        # if basket['E'] >= 2 and basket["B"] >= 1:
        #     e_deals = basket['E'] / 2
        #     if e_deals > basket['B']:
        #         e_deals = basket['B']
        #
        # b_deals = (basket['B'] - e_deals) / 2
        #
        # f_deals = basket['F'] / 3  # Equivalent to 2 + 1
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
