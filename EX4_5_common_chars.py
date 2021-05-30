# EX:4 5) Find all common characters between two strings.

import sys

if len(sys.argv) != 3:
    print(f"Argument error\n number of arguments {len(sys.argv)}, expected 3")
    print(f" Usage {sys.argv[0]} <first_string> <second_string>")
    exit(1)

first_string    = sys.argv[1]
second_string   = sys.argv[2]

common_chars = []
for char in first_string:
    if char in second_string:
        common_chars.append(char)

print(f"common characters {common_chars}")

common_chars = set(common_chars)
common_chars = list(common_chars)
print(f"common characters {common_chars}")
