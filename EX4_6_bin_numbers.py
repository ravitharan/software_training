# # EX:4 6) Create 100 random numbers between 1 to 100 and group every number into bins
# with intervals of 10. Eg bins are 1-10, 11-20,..91-100.

import random

MAX_NUMBER_VALUE    = 100
DIVIDING_RANGE      = 20

# Create 100 random numbers between 1 to 100
numbers = random.sample(range(1, MAX_NUMBER_VALUE + 1), 100)


NUM_BINS = int(MAX_NUMBER_VALUE / DIVIDING_RANGE)
# Create required bins of empty list to put numbers
bins = []
for i in range(NUM_BINS):
    bins.append([])

for num in numbers:
    for bin_num in range(NUM_BINS):
        bin_range = (bin_num + 1) * DIVIDING_RANGE
        if num < bin_range:
            bins[bin_num].append(num)
            # put the number one bin only
            break

for abin in bins:
    print(str(abin))
