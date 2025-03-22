import math
import random
import string
def exercise10_2_1(a, b, c):
    D = b * b - 4 * a * c
    if D > 0:
        x_1 = (-b + math.sqrt(D)) / (2 * a)
        x_2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Два корня: {x_1}, {x_2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Один корень: {x}")
    else:
        print("Нет")


# exercise10_2_1(3, 12, 3)

def exrrcise10_2_3():
    matrix = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ]

    for row in matrix:
        row.append(random.randint(1, 100)) 

    print(matrix)

# exrrcise10_2_3()


def exercise10_3_2(num):
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    all_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = lowercase + uppercase + digit + special
    while 1:
        if len(password) < num:
            password += random.choice(all_symbols)
        else:
            break
    
    random.shuffle(list(password)) 
    print("".join(password)) 

# exercise10_3_2(10)

def exersice10_3_4(str):
    result = eval(str)
    print(result) 


# exersice10_3_4("10 *6")

def exrrcise10_3_5():
    matrix = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ]

    for row in matrix:
        row.append(random.randint(1, 100))

    new_row = [random.randint(1, 100) for _ in range(len(matrix[0]))] 
    matrix.append(new_row)


    print(matrix)

# exrrcise10_3_5()


def exrrcise10_5_2(num):
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    column_values = [row[num] for row in matrix]
    print(column_values)  

# exrrcise10_5_2(2)