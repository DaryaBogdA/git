import math
from decimal import Decimal
import re
import itertools

def check(number):
    number = Decimal(str(number))
    if number == number.quantize(1):
        return 1
    else:
        return 0

def exercise10_6_1():
    for i in range(1, 10):
        a = i
        for j in range(1, 10):
            b = j
            for k in range(1, 10):
                c = k
                D = b * b - 4 * a * c
                if D > 0:
                    x_1 = (-b + math.sqrt(D)) / (2 * a)
                    x_2 = (-b - math.sqrt(D)) / (2 * a)
                    if check(x_1) and check(x_2):
                        print(f"{a}x^2 + {b}x + {c}")


# exercise10_6_1()
    



def get_permutations(str):
    def permutations(start_word, word, results):
        if len(word) == 0:
            results.append(start_word)
        else:
            for i in range(len(word)):
                new_prefix = start_word + word[i]
                new_word = word[:i] + word[i+1:]
                permutations(new_prefix, new_word, results)

    results = []
    permutations("", str, results)
    return results

def exercise10_7_1():
    word = input("Введите слово: ")
    permutations = get_permutations(word)

    for permutation in permutations:
        print(permutation)


# exercise10_7_1()

def exercise10_7_3():
    matrix = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    result = [0] * 5
    for i in range(5):
        for j in range(5):
            result [i] += matrix[j][i]
    print(result)

# exercise10_7_3()


def exercise10_8_1(password):
    count = 0
    if len(password) < 8:
        count += 1
    if password.islower():
        count += 1
    what = False
    for char in password:
        ascii_code = ord(char)
        if  (48 <= ascii_code <= 57 or 65 <= ascii_code <= 90 or 97 <= ascii_code <= 122):
            what = True
        else:
            what = False
    if what:
        count += 1

    if count == 0:
        print("CЛожный")
    if count == 1:
        print("Средний")
    if count == 2:
        print("Легкий")
    if count == 3:
        print("Очень легкий")

# password = input("Введите пароль ")
# exercise10_8_1(password)

def exercise10_8_2(arr):
    for permutation in itertools.permutations(arr):
        print(permutation)

exercise10_8_2([2, 4, 6])





