
# Write a python function to convert roman numerals into decimal value.
# I   1
# V   5
# X   10
# L   50
# C   100
# D   500
# M   1000

import sys

def char_to_num(char):
    if char == 'I':
        num = 1
    elif char == 'V':
        num = 5
    elif char == 'X':
        num = 10
    elif char == 'L':
        num = 50
    elif char == 'C':
        num = 100
    elif char == 'D':
        num = 500
    elif char == 'M':
        num = 1000
    return num

if len(sys.argv) != 2:
    print(f"Argument error\nUsage: {sys.argv[0]}")
    exit(1)

roman = sys.argv[1].upper()

decimal = 0
i = 0
skip_next_char = False
for i in range(len(roman)):
    if not skip_next_char:
        num = char_to_num(roman[i])
        if (i < len(roman) - 1):
            next_num = char_to_num(roman[i+1])
            if (num < next_num):
                num = next_num - num
                skip_next_char = True
        decimal += num

print(f"{roman} = {decimal}")


