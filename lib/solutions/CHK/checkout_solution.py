

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
        num_deals = items / discount
        return (num_deals, items - (num_deals * discount))

    def _double_multibuy(items, discount_low, discount_high):
        num_deals_high = items / discount_high
        remaining = items - discount_high * num_deals_high
        num_deals_low = remaining / discount_low
        remaining = remaining - discount_low * num_deals_low
        return (num_deals_high, num_deals_low, remaining)

    def _bogof_diff(items, discounted_items, threshold):
        if items >= threshold and discounted_items >= 1:
            num_deals = items / threshold
            if num_deals > discounted_items:
                num_deals = discounted_items
        remaining_items = items - num_deals * threshold
        remaining_discounted_items = discounted_items - num_deals
        return (num_deals, remaining_items, remaining_discounted_items)

    # def _bogof_same(items, threshold):
    #     if items >= threshold + 1:
    #         num_deals = items / (threshold + 1)
    #     remaining_items = items - num_deals * (threshold + 1)
    #     return (num_deals, remaining_items)

    # def _check_off_items_in_deal(rem_basket, item_key, num_items):
    #     rem_basket[item_key] = rem_basket[item_key] - num_items
    #     if rem_basket[item_key] < 0:
    #         print "Have removed more items from deals than existed"
    #         raise ValueError
    #     return rem_basket

    def _check_for_deals(basket):
        rem = basket.copy()
        deals = dict()

        deals['5A'], deals['3A'], rem['A'] = \
            _double_multibuy(rem['A'], 3, 5)
        print deals, rem
        deals['2E'], rem['E'], rem['B'] = _bogof_diff(rem['E'], rem['B'], 2)
        deals['2B'], rem['B'] = _multibuy(rem['B'], 2)
        deals['2F'], rem["F"] = _multibuy(rem['F'], 2+1)

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

        # deals = {'A': a_deals,
        #          'B': b_deals,
        #          'E': e_deals,
        #          'F': f_deals,
        #          'AAAAA': multi_a_deals}
        return (deals, rem)

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

    deals, remaining_basket = _check_for_deals(basket)

    """ This sum could be shortened, but I will leave it long for now
        to see what is going on """
    def _compute_cost_deals(deals):
        deal_prices = {'3A': 130, '5A': 200,
                       '2E': 80,
                       '2F': 20,
                       ''}
        return cost

    def _compute_cost_remaining(rem):
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
                  'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
                  'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
                  'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
                  'Y': 10, 'Z': 50}
        return sum(prices[k]*rem[k] for k in prices)

    # cost = (deals['A'] * 130 + deals['B'] * 45 +
    #         deals['AAAAA'] * 200 + deals['F'] * 20 +
    #         (basket['A'] - 3 * deals['A'] - 5 * deals['AAAAA']) * 50 +
    #         (basket['B'] - 2 * deals['B'] - deals['E']) * 30 +
    #         basket['C'] * 20 +
    #         basket['D'] * 15 +
    #         basket['E'] * 40 +
    #         (basket['F'] - 3 * deals['F']) * 10)

    total_cost = (_compute_cost_deals(deals) +
                  _compute_cost_remaining(remaining_basket))
    return total_cost
