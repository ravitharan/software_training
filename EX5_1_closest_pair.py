# Create a random number list of N (argument to the function) entries between 1
# and 100 and find the closest number pair. Use two methods without using sort
# and using sort.
import random
import sys
#find closest pair
def closet_pair_num_1(n):
    import random
    a = random.sample(range(1, 100), n)
    print(a)
    b = sorted(a)
    print(b)
    num1 = a[0]
    num2 = a[1]
    min = num2 - num1
    for i in range(n-1):
        if (min > (b[i+1]-b[i])):
            min = (b[i+1]-b[i])
            num1 = b[i]
            num2 = b[i+1]
    return [num1, num2]

def closet_pair_num_2(n):
    a = random.sample(range(1, 100), n)
    print(a)
    min = 100
    num1 = a[0]
    num2 = a[1]
    min = num2 - num1
    for i in range(n-1):
        for x in range(i+1, n-1):
            if (min > abs(a[i]-a[x])):
                min = abs(a[i]-a[x])
                num1 = a[i]
                num2 = a[x]
    return [num1, num2]

if len(sys.argv) != 2:
    print(f"Argument error\nUsage {sys.argv[0]} <list_size>")
    exit(1)

n = int(sys.argv[1])

print(closet_pair_num_1(n))

print(closet_pair_num_2(n))
