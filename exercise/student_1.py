import random
import sys

"""1 In python interactive mode, what is the output for the following expressions,
1 msg = 'Hello'; var = 3 * msg + msg;
What will be the var in the above expression?"""
#1
def question_1():
    msg = 'Hello';
    var = 3 * msg + msg;
    print(var)

"""2 msg = 'Hello'
Give an expression to get the string “Hello Hello Hello Hello Hello” using variable
msg.
"""
#2
def question_2():
    msg="hello"" ";
    var=4*msg+msg;
    print(var," " )

"""3 msg = 'Hello python world'
Give two expressions using variable msg only to get the string “python world”.
"""
#3
def question_3():
    msg = 'Hello python world'
    print(msg[6:])

"""4 ' ', ‘\t’ and ‘\n’ are three white space characters. If msg = “hello”, what is
the display for print(f"{msg}\n\t{msg}")"""
#4
def question_4():
    msg="hello"
    print(f"{msg}\n\t{msg}")

"""5 msg = 'hello'
what is the print expression to get following display using variable msg,"""
#5
def question_5():
    msg="hello"
    print(f"{msg}\n\t{msg}\n\t\t{msg}\n\t{msg}\n{msg}")

"""6 If msg = “hello python world”, how would you print following two messages
Hello Python World
hELLO pYTHON wORLD
(hint: run dir(str) and find which function can be used for the above purpose)
"""
#6
def question_6():
    msg="hello python world"
    print(msg.title ( ))

#Find the total of following sequence numbers using range() and for loop,
#7 : 1, 2, 3, …, 99, 100
def question_7():
    count = 0
    for x in range (1,100):
        count+= x
    print(count)

#8 : 1, 3, 5, …, 97, 99
def question_8():
    count = 0
    for x in range (1,100):
        if x%2 != 0:
            count = count+ x
    print(count)

#9 : 2, 4, 6, …, 98, 100
def question_9():
    count = 0
    a=[]
    for x in range (1,100):
        if x%2 == 0:
            count = count+ x
    print(count)

#Create a 1000 random number list with the value between 1 and 100 (inclusive). Using this list,
#10 : How many numbers are between 1 and 50 (inclusive)
def question_10():
    random_List=[]
    for x in range(100):
        random_no = random.randint(1,100)
        random_List.append(random_no)

    count=0
    for m in random_List:
        if m < 50:
            count=count+1
    print(count)

#11 : How many numbers are above 50
def question_11():
    random_List=[]
    for x in range(100):
        random_no = random.randint(1,100)
        random_List.append(random_no)

    count=0
    for m in random_List:
        if m >= 50:
            count=count+1
    print(count)

#12 : Total of all numbers
def question_12():
    random_List=[]
    for x in range(100):
        random_no = random.randint(1,100)
        random_List.append(random_no)

    count=0
    for m in random_List:
        count=count+m
    print(count)

#13 : Average of the numbers.
def question_13():
    random_List=[]
    for x in range(100):
        random_no = random.randint(1,100)
        random_List.append(random_no)

    random_List_count=0
    for m in random_List:
        random_List_count = random_List_count+m
    print(random_List_count)
    print(random_List_count/len(random_List))

#14 Write a function right_triangle(height) to print the following pattern taking the height as argument.
def question_14():
    for a in range(0,9):
        for b in range(0,a+1):
            print("*", end="")
        print()

#15 Write a function inv_right_triangle(height) to print the following pattern taking the height as argument.
def question_15():
    for c in range(11,0,-1):
        for d in range(0,c-1):
            print("*",end="")
        print()

#16 Write a function to determine if a given number is a prime number or not. Hint: If any number between 2 to (number-1) cannot divide the given number, it is a prime number.
def question_16():
    no=int(input("Enter the number :"))
    if 1<no:
         for x in range(2,no):
              if(no%x==0):
                   print(no,"this number is not prime number")
                   break
              else:
                   print(no,"this number is prime number")
                   break

#17 Write function to return number of vowels of a string
def question_17():
    a=input("ENTER A STRING :")
    n=0
    for x in a:
         if x in "AaEeIiOoUu":
              n+=1
    print("The string number of vowels in",a,"is",n)

#18 Create a random number list of 20 and reverse its entries.
def question_18():
    a=[random.randint(1,100)for a in range(20)]
    print(a)
    a.reverse()
    print(a)

#19 Write a function right_triangle_2(height) to print the following pattern taking the height as argument.
def question_19():
    for x in range(0,10):
        for m in range(0,10-x):
            print(" ",end=" ")
        for n in range(0,x+1):
            print("*",end=" ")
        print()
#20 Write a function isosceles_triangle(height) to print the following pattern taking the height as argument.
def question_20():
    for i in range(1,21):
         for j in range(1,21-i):
              print(" ",end='')
         for k in range(1,i+1):
              print("* ",end='')
         print( )

#21 Write a function inv_isosceles_triangle(height) to print the following pattern taking the height as argument.
def question_21():
    rows = 9
    k = 2*rows - 2
    for a in range(rows, -1, -1):
        for b in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for b in range(0, a+1):
            print("*", end=" ")
        print("")

#22 Write a function diamond(width) to print the following pattern taking the width as an argument.
def question_22():
    rows = 10
    m = 2 * rows - 2
    for n in range(0, rows):
        for x in range(0, m):
            print(end=" ")
        m = m - 1
        for x in range(0, n + 1):
            print("* ", end="")
        print("")

    m = rows - 2

    for n in range(rows, -1, -1):
        for x in range(m, 0, -1):
            print(end=" ")
        m = m + 1
        for x in range(0, n + 1):
            print("* ", end="")
        print("")

#23

#24 Write a function diamonds(count, width) to print the following pattern taking the width as an argument.
def question_23():
    a=input("ENTER A STRING :")
    b=input("ENTER A STRING :")
    x=set(a)
    y=set(b)
    lst=list(x&y)
    print('common letters:{}'.format(lst))

#25 number_guess.py is a small program, are you able to find out, what is it doing? Can you create another similar program?

#26 #24 Write a function diamonds(count, width) to print the following pattern taking the width as an argument.
def question_24():
    a=input("ENTER A STRING :")
    b=input("ENTER A STRING :")
    x=set(a)
    y=set(b)
    lst=list(x&y)
    print('common letters:{}'.format(lst))

#27 https://docs.google.com/document/d/14tjl3ffSrqQ7fA77pRx9oUK5taDkdyCEE-T0NOZk9hM/edit#
def question_25():
    random_list=[]
    for a in range(1,100):
        x = random.randint(1,100)
        random_list.append(x)
    print(random_list)
    List1=[]
    List2=[]
    List3=[]
    List4=[]
    List5=[]
    List6=[]
    List7=[]
    List8=[]
    List9=[]
    List10=[]

    for m in random_list:
        if 11 > m:
            List1.append(m)
        if 21 > m:
            List2.append(m)
        if 11 > m:
            List3.append(m)
        if 31 > m:
            List4.append(m)
        if 41 > m:
            List5.append(m)
        if 51 > m:
            List6.append(m)
        if 61 > m:
            List7.append(m)
        if 71 > m:
            List8.append(m)
        if 81 > m:
            List9.append(m)
        if 91 > m:
            List10.append(m)


    print("1-10 :",List1)
    print("11-20 :",List2)
    print("21-30 :",List3)
    print("31-40 :",List4)
    print("41-50 :",List5)
    print("51-60 :",List6)
    print("61-70 :",List7)
    print("71-80 :",List8)
    print("81-90 :",List9)
    print("91-100 :",List10)

#28

#29

#30 Leap or common year
def question_26():
    year = int(input("Enter Year :"))
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print(year,"is leep year")
            else:
                print(year,"not an leep year")
        else:
            print(year,"not an leep year")
    else:
        print(year,"not an leep year")

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Argument error")
        print(f"Usage: {sys.argv[0]} <question_number>")
        exit(1)

    qn_num = int(sys.argv[1])
    question = f"question_{qn_num}"
    function = eval(question)
    function()
