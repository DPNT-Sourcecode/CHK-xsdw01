filepath = '''/Users/MichaelHook/challenge/tdl-runner-python/
              lib/solutions/CHK/price_list.txt'''
fh = open(filepath)
for line in fh:
    if line.startswith('|'):
        print line
