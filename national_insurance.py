import sys

EMPOLOYER_NATIONAL_INSURANCE = {
                                'A': [0, 0.12, 0.02],
                                'B': [0, 0.0585, 0.02],
                                'H': [0, 0.12, 0.02],
                                'J': [0, 0.02, 0.02],
                                'M': [0, 0.12, 0.02],
                                'Z': [0, 0.02, 0.02]
                                }

EMPOLOYER_NATIONAL_INSURANCE_2 = {
                                'A': [0, 0.138, 0.138],
                                'B': [0, 0.138, 0.138],
                                'C': [0, 0.138, 0.138],
                                'H': [0, 0, 0.138],
                                'J': [0, 0.138, 0.138],
                                'M': [0, 0, 0.138],
                                'Z': [0, 0, 0.138]
                                }


def tax_calculation(SALARY,CATEGORY):
    """
        salary: 783, Tax: 93.96
        salary: 33.0, Tax: 94.61999999999999
        Total Salary: 1000.0
        Total Tax : 94.61999999999999 
    """

    tax = 0     

    for i, persntage in enumerate(EMPOLOYER_NATIONAL_INSURANCE[CATEGORY]):
        if SALARY < 184 and i == 0:
            tax += (SALARY*persntage)
        elif 184 < SALARY < 967 and i == 1:
            tax += ((SALARY-184)*persntage)
            print(f'salary: {(SALARY-184)}, Tax: {tax}')
        elif SALARY > 967 and i == 1:
            tax += ((967-184)*persntage)
            print(f'salary: {(967-184)}, Tax: {tax}')
        elif SALARY > 967 and i == 2:
            tax += ((SALARY-967)*persntage)
            print(f'salary: {(SALARY-967)}, Tax: {tax}')

    print(f'Total Salary: {SALARY} \nTotal Tax : {tax} \n')          

    return tax

def tax_calculation_2(SALARY,CATEGORY):
    """
        salary: 783, Tax: 108.054
        salary: 33.0, Tax: 112.608
        Total Salary: 1000.0
        Total Tax : 112.608 
    """
    
    tax_2 = 0     

    for i, persntage in enumerate(EMPOLOYER_NATIONAL_INSURANCE_2[CATEGORY]):
        if SALARY < 170 and i == 0:
            tax_2 += (SALARY*persntage)
        elif 170 < SALARY < 967 and i == 1:
            tax_2 += ((SALARY-184)*persntage)
            print(f'salary: {(SALARY-184)}, Tax: {tax_2}')
        elif SALARY > 967 and i == 1:
            tax_2 += ((967-184)*persntage)
            print(f'salary: {(967-184)}, Tax: {tax_2}')
        elif SALARY > 967 and i == 2:
            tax_2 += ((SALARY-967)*persntage)
            print(f'salary: {(SALARY-967)}, Tax: {tax_2}')

    print(f'Total Salary: {SALARY} \nTotal Tax : {tax_2}')          

    return tax_2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Argument error')
        exit(1)

CATEGORY = sys.argv[1]
SALARY = float(sys.argv[2])
tax = tax_calculation(SALARY,CATEGORY)
tax_2 = tax_calculation_2(SALARY,CATEGORY)
