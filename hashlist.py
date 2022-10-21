import random

hashlist = []

# make a hash list for 7 columns, 6 rows, and 2 colors

for i in range(2):
    for j in range(7):
        for k in range(6):
            hashlist.append(random.randint(0, 2**64))