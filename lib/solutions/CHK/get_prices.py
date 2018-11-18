filepath = ('/Users/MichaelHook/challenge/tdl-runner-python/' +
            'lib/solutions/CHK/price_list.txt')
fh = open(filepath)

price_list = {}
for line in fh:
    if line.startswith('|'):
        if not line.split()[1].startswith('Item'):
            print line.split()[1]
