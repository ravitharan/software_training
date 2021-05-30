# EX:4 3) Create a random number list of 20 and reverse its entries

import random

NUM_ITEMS = 20

# Create 20 random numbers between 1 to 100
numbers = random.sample(range(1, 101), NUM_ITEMS)

# Method1: Using for loop
reverse = []

for i in range(NUM_ITEMS):
    num = numbers[NUM_ITEMS - 1 -i]
    reverse.append(num)

print(f"Original list {numbers}\nReverse list  {reverse}")

# Method2: Reverse with silicing is one line code
rev_numbers = numbers[::-1]
print(f"Original list {numbers}\nReverse list  {rev_numbers}")
