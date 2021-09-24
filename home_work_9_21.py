# 22)

def diamond_creater(diamond_line_size):
    def odd_number_anlaysis():      # This function analyses the odd numbers between user input
        analys = []
        for odd in range(diamond_line_size   , 0 , -2): 
            analys.append(odd)
        return analys

    analys = odd_number_anlaysis()

    def get_line_size_of_straight_triangle():   # This function gets the first straight triangle's line size
        length_of_analys = len(analys)
        line_size_of_straight_triangle = diamond_line_size  - (length_of_analys - 1)
        return line_size_of_straight_triangle

    line_size_of_straight_triangle = get_line_size_of_straight_triangle()

    def get_line_size_of_inverse_triangle():   # This function gets the second inverse triangle's line size
        line_size_of_inverse_triangle = diamond_line_size 
        line_size_of_inverse_triangle = line_size_of_inverse_triangle - line_size_of_straight_triangle
        return line_size_of_inverse_triangle

    line_size_of_inverse_triangle = get_line_size_of_inverse_triangle()

    # This code get the odd number between triangle number for printing a triangle
    triangularNumber = int(line_size_of_straight_triangle*(line_size_of_straight_triangle+1)/2)           
    graphic_list = []                                 
    for i in range(1 , triangularNumber + 1 , 2):
        graphic_list.append(i)                      

    def create_straight_triangle():   # This function create straight triangle
        space  = line_size_of_straight_triangle - 1
        m = 0
        straight_triangle = ""
        for x in range(space, -1 , -1):
            y = x * " "
            y += graphic_list[m] * "*"
            straight_triangle += "\n" + y
            m = m + 1
        straight_triangle = straight_triangle[1:]
        straight_triangle = straight_triangle + "\n"
        return straight_triangle

    straight_triangle = create_straight_triangle()

    def create_inverse_triangle():  # This function create inverse triangle
        space  = line_size_of_inverse_triangle - 1
        m = line_size_of_inverse_triangle - 1
        inverse_triangle = ""
        for x in range(1 , space+2):
            y = x * " " 
            y += graphic_list[m] * "*"
            inverse_triangle += y + "\n"
            m = m - 1
        inverse_triangle = inverse_triangle[0:len(inverse_triangle) - 1]
        
        return inverse_triangle

    inverse_triangle = create_inverse_triangle()
    return (straight_triangle + inverse_triangle)
    
"""        
   *
  ***
 *****
*******
 *****
  ***
   *
    
"""


"""  1      1     0
     *      *
     3      2     1
     *      * 
    ***    ***    *
     *
     5      3     2
     *      *
    ***    ***   ***
   *****  *****   *
    ***
     *
   
     7          4
   diamond  triangle
   9  5
"""



# 24)

def two_string_intersection(first_string , second_string):
    first_string_set  = set(first_string)
    second_string_set = set(second_string)
    intersection_set = first_string_set.intersection(second_string_set)
    intersection_string = ""
    for i in intersection_set:
        intersection_string = intersection_string + i
    return intersection_string

#25)
# this function doesn't take your_number for calculation only takes sum_12 , sum_23 , sum_13
def guess_num(Your_number , sum12 , sum23 , sum13):
    for i in range(100 , 1000):
        analys  = str(i)
        sum_12 = int(analys[0]) + int(analys[1])
        sum_23 = int(analys[1]) + int(analys[2])
        sum_13 = int(analys[0]) + int(analys[2])
        if (sum_12 == sum12):
            if (sum_23 == sum23):
                if (sum_13 == sum13):
                    return int(analys)
    
#27)
import random
x = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = 0
n = 1
for i in range(10):
    exec(f'bin_{x[m]}_{x[n]} = []')
    m += 1
    n += 1
for i in range(100):
    random_num= round(random.uniform(1,100), 1)
    if (random_num >= 1 and random_num < 10):
        bin_1_10.append(random_num)
    elif (random_num >= 10 and random_num < 20):
        bin_10_20.append(random_num)
    elif (random_num >= 20 and random_num < 30):
        bin_20_30.append(random_num)
    elif (random_num >= 30 and random_num < 40):
        bin_30_40.append(random_num)
    elif (random_num >= 40 and random_num < 50):
        bin_40_50.append(random_num)
    elif (random_num >= 50 and random_num < 60):
        bin_50_60.append(random_num)
    elif (random_num >= 60 and random_num < 70):
        bin_60_70.append(random_num)
    elif (random_num >= 70 and random_num < 80):
        bin_70_80.append(random_num)
    elif (random_num >= 80 and random_num < 90):
        bin_80_90.append(random_num)
    elif (random_num >= 90 and random_num < 100):
        bin_90_100.append(random_num)
final_list = []
m = 0
n = 1
for f in range(10):
    exec(f'final_list.append(bin_{x[m]}_{x[n]})')
    m += 1
    n += 1
#print(final_list)

    
#28)

import random
def closest_number_pair(N):
    Randomlist = random.sample(range(1, 101), N)
    
    def selectionSort(List):
        for i in range(len(List) - 1):
            minimum = i
            for j in range( i + 1, len(List)):
                if(List[j] < List[minimum]):
                    minimum = j
            if(minimum != i):
                List[i], List[minimum] = List[minimum], List[i]
        return List
    
    sorted_list = selectionSort(List = Randomlist)
   
    m , n , difference = 0 , 1 , []
    for s in range(N-1):
        difference.append(sorted_list[n] - sorted_list[m])
        m += 1
        n += 1
    diff_min = difference.index(min(difference))
    
    return (sorted_list[diff_min] , sorted_list[diff_min + 1])

#29)

def RtoD(R):
    r  = { "I":1 , "V":5 , "X" :10 , "L":50 , "C":100 , "D":500 , "M":1000}
    cal_list = []
    for i in R:
        cal_list.append(r[i])
    if len(cal_list) == 1:
        return cal_list[0]
    else:
        def split_rep(s):
            L = []
            temp = s[0]
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    temp += s[i]
                else:
                    L.append(temp)
                    temp = s[i]
                if i == len(s)-1:
                    L.append(temp)
            return L
        split_list = split_rep(cal_list)
        x = 0
        for i in range(len(split_list) - 1):
            if split_list[len(split_list) - 1] < split_list[len(split_list) - 2]:
                x = split_list[len(split_list) - 1] + split_list[len(split_list) - 2]
                split_list.pop()
                split_list.pop()
                split_list.append(x)
            else:
                x = split_list[len(split_list) - 1] - split_list[len(split_list) - 2]
                split_list.pop()
                split_list.pop()
                split_list.append(x)
    
        return split_list[0] 
        

            
        
            
    
        

        
        
        
        



    
    
        



