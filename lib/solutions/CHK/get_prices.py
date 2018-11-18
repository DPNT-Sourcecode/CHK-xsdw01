import os


file_dir = os.path.dirname(os.path.realpath('__name__'))
print file_dir

filepath = '/Users/MichaelHook/challenge/tdl-runner-python/lib/solutions/CHK/price_list.txt'
fh = open(filepath)
for line in fh:
    print line
