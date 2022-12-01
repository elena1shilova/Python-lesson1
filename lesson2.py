#---------------Number1-------------------
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11
#Решение
# a = list(map(str, input('Введите вещественное число: ')))
# print(a)
# r = 0
# for e in a:
#     if e == '.' or e == ',':
#         e = 0
#     r = r + int(e)
# print(r)

#---------------Number2-------------------
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math
# N = int(input('Введите число: '))
# i = 1
# q = 1
# while i <= N:
#     q = q * i
#     i += 1
# print(q)

#---------------Number3-------------------
# Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)
# n = float(input('Введите число: '))
# i = 1
# q = 0
# while i <= n:
#     q = q + (1 + 1 / i)**i
#     i += 1
# print(q)

#---------------Number4-------------------
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
# from random import randint
# from array import *
# my_array = array('i',[0]*10)
# i = 0
# while i < 10:
#     my_array[i] = randint(-10, 11)
#     print(my_array[i], end=' ')
#     i+=1
# print()
# a = int(input('Введите позицию первого числа от 1 до 10: '))
# b = int(input('Введите позицию второго числа от 1 до 10: '))
# print(my_array[a-1] * my_array[b-1])

#---------------Number5-------------------
# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
# from random import randint
# from array import *
# a = 10
# my_array = array('i',[0]*a)
# i = 0
# while i < a:
#     my_array[i] = randint(0, a)
#     print(my_array[i], end=' ')
#     i+=1
# my_array2 = array('i',[0]*a)
# z = 0
# b = a-1
# print()
# while z < a:
#     my_array2[z] = my_array[b]
#     print(my_array2[z], end=' ')
#     z+=1
#     b-=1
