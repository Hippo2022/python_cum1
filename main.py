# # Создать python модуль для реализации ввода через клавиатуру целочисленных значений
# # Добавить функционал конвертации во float и str. Вывести результат на печать.
# # Создать python модуль для реализации ввода через клавиатуру дробных (с плавающей запятой) значений.
# # Добавить функционал конвертации в int и str. Вывести результат на печать.

# my_int = int(input('Enter any integer number: '))
# print('my_int: ', my_int)
# print('type(my_int): ', type(my_int))
# my_float = float(my_int)
# print('my_float: ', my_float)
# print('type(my_float): ', type(my_float))
# my_str = str(my_int)
# print('my_str: ', my_str)
# print('type(my_str): ', type(my_str))
#
# my_float1 = input('Enter any float number: ')
# my_float1 = float(my_float1)
# print('my_float1: ', my_float1)
# print('type(my_float1): ', type(my_float1))
# my_int1 = int(my_float1)
# print('my_int1: ', my_int1)
# print('type(my_int1): ', type(my_int1))
# my_str1 = str(my_float1)
# print('my_str1: ', my_str1)
# print('type(my_str1): ', type(my_str1))

# # Из двух случайных чисел, одно из которых четное, а другое нечетное,
# # определить и вывести на экран нечетное число.

# from random import random
#
# a = int(random() * 1000)
# b = int(random() * 1000)
# if a % 2 and b % 2 or a % 2 == 0 and b % 2 == 0:
#     a += 1
# print('random_1:', a, 'random_2:', b)
# if a % 2:
#     print('odd number is random_1: ', a)
# else:
#     print('odd number is random_2: ', b)

# # Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
# print('Enter three numbers: ')
# a = int(input())
# b = int(input())
# c = int(input())
#
# if b < a < c or c < a < b:
#     print('Average between numbers: ', a)
# elif a < b < c or c < b < a:
#     print('Average between numbers: ', b)
# else:
#     print('Average between numbers: ', c)

# # Вводятся три целых числа. Определить какое из них наибольшее.

# print('Enter three numbers, and we will find the maximum of them: ')
# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
# print('max=', m)


# # Вводятся координаты (x;y) точки и радиус круга (r). Определить принадлежит ли данная точка кругу,
# # если его центр находится в начале координат.

from math import hypot

x = float(input('x='))
y = float(input('y='))
r = float(input('r='))
h = hypot(x, y)
print('Расстояние до точки от начала координат (Как гипотенуза пр. треугольника) равно: ', round(h, 2))
if h > r:
    print('точка не принадлежит кругу')
else:
    print('точка принадлежит кругу')


# # Дана следующая функция y=f(x):
# # y=2x-10, если x>0
# # y = 0, если x = 0
# # y = 2 * |x| - 1, если x < 0
# # Требуется найти значение функции по переданному x.

# x = int(input('x= '))
# if x > 0:
#     y = 2 * x - 10
# elif x == 0:
#     y = 0
# else:
#     y = 2 * abs(x) - 1
# print('y=', y)

# # Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.

# x = int(input('x= '))
# y = int(input('y= '))
# if x > 0 and y > 0:
#     print('The point is in the first quarter')
# elif x < 0 and y > 0:
#     print('The point is in the second quarter')
# elif x < 0 and y < 0:
#     print('The point is in the third quarter')
# elif x > 0 and y < 0:
#     print('The point is in the fourth quarter')

# # Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом,
# # а также остаток (если он есть) и частное (в любом случае).

# print('№1 Я нашел решение, но не разобрался как реализовать :) ')
# a = int(input('a= '))
# b = int(input('b= '))
# if a % b == 0:
#     print('%d делится на %d' % (a, b))
# else:
#     print('%d не делится на %d' % (a, b))
#     print('Остаток: %d' % (a % b))
# print('Частное: %d' % (a // b))


# # Задача. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# # составленного из этих отрезков. Если такой треугольник существует, то определить,
# # является ли он разносторонним, равнобедренным или равносторонним.

# # Решение. Треугольник существует только тогда, когда сумма двух его сторон больше третьей
# # Если хотя бы в одном случае сторона окажется больше либо равна сумме двух других,
# # то треугольника с такими сторонами не существует.

# print('Укажите стороны треугольника:')
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
#
# if a + b > c and a + c > b and b + c > a:
#     print('Треугольник существует')
#     if a == b == c:
#         print('Треугольник равносторонний')
#     if a == b or a == c or b == c:
#         print('Треугольник равнобедренный')
#     else:
#         print('Треугольник разносторонний')
# else:
#     print('Треугольник не существует')
