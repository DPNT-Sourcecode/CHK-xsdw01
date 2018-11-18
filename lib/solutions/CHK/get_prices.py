import os


file_dir = os.path.dirname(os.path.realpath('__name__'))
print file_dir

# filepath = 'price_list.txt'
fh = open(filepath)
for line in fh:
    print line
