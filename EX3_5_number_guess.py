#!/usr/bin/env python3

input("Guess a number between 100 and 999 and press enter: ")

in_msg = input("What is the sum of first two digits (eg. for 213, it is 2+1 = 3): ")
sum_12 = int(in_msg)

in_msg = input("What is the sum of last two digits (eg. for 213, it is 1+3 = 4): ")
sum_23 = int(in_msg)

in_msg = input("What is the sum of first digit and third digit (eg. for 213, it is 2+3=5): ")
sum_13 = int(in_msg)

guess = 0

for n in range(100, 1000):
    a = n
    c = a % 10
    a //= 10
    b = a % 10
    a //= 10

    if (a+b == sum_12) and (b+c == sum_23) and (a+c == sum_13):
        guess = n

if guess == 0:
    print("You lied!")
else:
    print(f"Answers is {guess}")
