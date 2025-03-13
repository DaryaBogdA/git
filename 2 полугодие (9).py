import random
import re
def exercise10_1_1 (str):
    result = ""
    if str[-1] == "o" or str[-1] == "x" or str[-1] == "ss" or str[-1] == "sh" or str[-1] == "ch" or str[-1] == "s":
        result = str + "es"
    elif str[-1] == "y":
        result = str[:-1] + "ies"
    else:
        result = str + "s"
        
    

    
    print(result)

# exercise10_1_1("potato")
# exercise10_1_1("lady")
# exercise10_1_1("bus")
# exercise10_1_1("cat")


def exercise10_1_4():
    matrix = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
    ]
    new_row = [random.randint(1, 100) for i in range(len(matrix[0]))]
    
    matrix.append(new_row)
    print(matrix)

# exercise10_1_4()

def exercise10_1_2():
    text = 'aaa bbb, ccc. Xxx- eee bbb, kkk!'
    word = re.sub(r'[^\w\s]', '', text)

    print(word) 

# exercise10_1_2()




def exercise10_10_2():
    n = int(input("Введите число "))

    arr = [i for i in range(n + 1)]

    arr[1] = 0

    i = 2
    while i <= n:
        if arr[i] != 0:
            j = i + i
            while j <= n:
                arr[j] = 0
                j = j + i
        i += 1

    arr = [i for i in arr if i != 0]
    print(arr)
# exercise10_10_2()

def exercise10_10_3():
    new_matrix = []
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]
    for j in range(5): 
        new_row = []    
        for i in range(5): 
            new_row.append(matrix[i][j]) 
        new_matrix.append(new_row)

    print(new_matrix)

# exercise10_10_3()