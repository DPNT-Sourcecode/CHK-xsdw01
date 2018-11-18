def get_price_list:
    filepath = ('/Users/MichaelHook/challenge/tdl-runner-python/' +
                'lib/solutions/CHK/price_list.txt')
    fh = open(filepath)

    price_list = {}
    for line in fh:
        if line.startswith('|'):
            if not line.split()[1].startswith('Item'):
                key = line.split()[1]
                value = line.split()[3]
                price_list[key] = value

    return price_list
