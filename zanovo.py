# # 1st program
# print((9 ** 0.5) * 5)
# # 2st program
# print(9.99 > 9.98 and 1000 != 1000.1)
# # 3st program
# print(2 * 2 + 2)
# print(2 * (2 + 2))
# print(2 * 2 + 2 == 2 * (2 + 2))
# # 4st program
# print(int((float('123.456') * 10) % 10))         # вывести не экран первую цифру после запятой (4)

# example = "Топинамбур"
# print(example[0])
# print(example[-1])
# print(example[int(len(example)/2):])
# print(example[::-1])
# print(example[1::2])

# dz = 12
# s_t = 1.5
# name_k = 'Python'
# t_1dz = s_t / dz
# print(' Курс:', name_k, "всего задач:", dz,', затрачено часов:', s_t, ", среднее время выполнения", t_1dz, 'часа.' )

# name = 'Diana'
# print(name)
# age = 28
# print(age)
# new_age = 29
# print(new_age)
# is_student = True
# print(is_student)

# my_string = input(' Как у вас дела? ')
# print(len(my_string))
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ',''))
# print(my_string[0])
# print(my_string[-1])

# my_string = input()
# print(len(my_string))
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(' ',''))
# print(my_string[0])
# print(my_string[-1]

# immutable_var = (1, 2, 4, True, 'work')
# print(immutable_var)
# mutable_list = [2, 4, False, 'house']
# print(mutable_list)
# mutable_list[2] = True
# print(mutable_list)

# my_dick = {'Diana': 89021548909, 'Tanya': 89228209301, 'Sveta': 89058992535}
# print(my_dick)
# print(my_dick.get('Diana'))
# print(my_dick.get('Viktor'))
# my_dick.update({'Viktor': 89228671757, 'Marya': 8922735463})
# print(my_dick)
# a = my_dick.pop('Diana')
# print(a)
# print(my_dick)
#
# my_set = {3, 6, 3, 45, 'ndfh', True, 876, 45}
# print(my_set)
# my_set.discard(6)
# my_set.add(345)
# my_set.add(5646)
# print(my_set)

# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# students = sorted(students)
# students = list(students)
# a = {}
#
# for i in range(len(students)):
#     average_grade = sum(grades[i]) / len(grades[i])
#     a[students[i]] = average_grade
# print(a)

# first = int(input('Введите целое число: '))
# second = int(input('Введите целое число: '))
# third = int(input('Введите целое число: '))
#
# if first != second != first:
#     print(0)
#
# elif first == second == third:
#     print(3)
#
# else:
#     print(2)

# import this

# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
#
# while i < len(my_list):
#     if my_list[i] > 0:
#         print(my_list[i])
#         i += 1
#
#     elif my_list[i] == 0:
#         i += 1
#         continue
#     else:
#         break
#

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in numbers:
#     is_primes = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_primes = False
#             break
#
#     if is_primes == True:
#         primes.append(i)
#     if is_primes == False:
#         not_primes.append(i)
#
# print('primes', primes)
# print('not_primes', not_primes)

# def get_matrix(n, m, value):
#     matrix = []
#     for _ in range(n):
#         p = []
#         for _ in range(m):
#             p.append(value)
#         matrix.append(p)
#     return matrix
#
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)

import random
# def random_numbers():
#     number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#     win1 = random.choice(number)
#     return win1
#
# win1 = random_numbers()
# print(win1)
#
# def resh_numbers(win1):
#     for i in range(1, win1):
#         for j in range(1+i, win1):
#             if win1 % (i+j) == 0:
#                 print(f'{i}{j}', end='')
#             else:
#                 continue
#
# resh_numbers(win1)

