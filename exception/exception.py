""" Example showing exception and handling it """

def crashing_square():
    num_str = input("Enter a number: ")
    number = int(num_str)
    result = number ** 2
    return result


def message_square():
    num_str = input("Enter a number: ")
    try:
        number = int(num_str)
        result = number ** 2
    except ValueError as e:
        print ("Invalid integer entered")
        print(e)
        result = 0
    return result


def general_message_square():
    num_str = input("Enter a number: ")
    try:
        number = int(num_str)
        result = number ** 2
    except Exception as e:
        print(e)
        result = 0
    return result

def right_square():
    done = False
    while not done:
        num_str = input("Enter a number: ")
        try:
            number = int(num_str)
            result = number ** 2
            done = True
        except ValueError:
            print ("Invalid integer re-enter.")
    return result


def line_count_crash_1(file_name):
    fp = open(file_name, "r")
    count = 0
    for line in fp:
        count += 1
    fp.close()
    return count


def line_count_crash_2(file_name):
    with open(file_name, "r") as fp:
        count = 0
        for line in fp:
            count += 1
    return count


def line_count(file_name):
    try:
        with open(file_name, "r") as fp:
            count = 0
            for line in fp:
                count += 1
    except Exception as e:
        print(e)
        count = -1
    return count
