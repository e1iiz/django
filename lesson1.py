# a= 13
# b=12
# if a>b:
#     print(a)
# elif a==b:
#     print('равен')
# else:
#     print(b)

#2
# for i in range(1, 101):
#     print(i)

# a='asabayy'
# b=a[0:3]
# c=a[0:4]
# print(c+b)

# print(sum(map(int, input().split())))

# word = input()

# # Превращаем слово в палиндром
# def make_palindrome(s):
#     # Превращаем строку в список символов, чтобы можно было изменять символы
#     s = list(s)
#     # Проходим по половине строки и делаем её симметричной
#     for i in range(len(s) // 2):
#         # Меняем символы, если они не совпадают
#         if s[i] != s[-i - 1]:
#             s[-i - 1] = s[i]
#     # Возвращаем строку как палиндром
#     return ''.join(s)

# # Выводим слово, если оно уже палиндром, или результат преобразования
# print(word if word == word[::-1] else make_palindrome(word))


import math
from functools import reduce

# Функция для нахождения наименьшего общего кратного двух чисел
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Функция для нахождения НОК списка чисел
def lcm_list(lst):
    return reduce(lcm, lst)

# Чтение входных данных
N = int(input())                 # Число задач
P = list(map(int, input().split()))  # Количество решивших задачи
Q = list(map(int, input().split()))  # Общее количество студентов на каждую задачу

# Находим НОК всех элементов списка Q
L = lcm_list(Q)

# Вычисляем наименьшее возможное количество студентов
students = max(L * P[i] // Q[i] for i in range(N))

# Выводим результат
print(students)
