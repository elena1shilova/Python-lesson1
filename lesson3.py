# ---------------Number1-------------------
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Решение
# from random import randint
# from array import *
# q = 7
# my_array = array('i',[0] * q)
# i = 0
# sum = 0
# while i < q:
#     my_array[i] = randint(0, q + 1)
#     print(my_array[i], end=' ')
#     if i % 2 != 0:
#         sum = sum + my_array[i]
#     i+=1
# print()
# print(sum)

# ---------------Number2-------------------
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# Решение
# from random import randint
# from array import *
# q = 5
# my_array = array('i', [0] * q)
# i = 0
# z = q-1
# while i < q:
#     my_array[i] = randint(0, q + 1)
#     print(my_array[i], end=' ')
#     i += 1
# i = 0
# print()
# if q % 2 == 0:
#     my_array2 = array('i', [0] * q/2)
#     while i < q/2:
#         my_array2[i] = my_array[i] * my_array[z]
#         print(my_array2[i], end=' ')
#         i += 1
#         z -= 1
# else:
#     my_array2 = array('i', [0] * int(q/2+1))
#     while i < int(q/2+1):
#         my_array2[i] = my_array[i] * my_array[z]
#         print(my_array2[i], end=' ')
#         i += 1
#         z -= 1

# ---------------Number3-------------------
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Решение
# from array import *
# my_array = array('d', [1.1, 1.2, 3.1, 5, 10.01])
# i = 0
# min = my_array[0] - int(my_array[0])
# max = my_array[0] - int(my_array[0])
# print(str(my_array[3]).split('.')[1])
# while i < len(my_array):
#     if int(str(my_array[i]).split('.')[1]) == 0:
#         print(my_array[i])
#         i+=1
#     else:
#         my_array[i] = my_array[i] - int(my_array[i])
#         if my_array[i] < min:
#             min = my_array[i]
#         if my_array[i] > max:
#             max = my_array[i]
#         i+=1
# print(round(max - min, 2))

# ---------------Number4-------------------
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# Решение
# a = 2
# my_list = list()
# while (a > 0) or (a > 1):
#     my_list.append(a%2)
#     a = int(a/2)
# my_list.reverse()
# print(my_list)
   
# ---------------Number5-------------------
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Решение
# k = 8
# q = 0
# w = 1
# my_list = list()
# my_list.append(q)
# my_list.append(w)
# my_list.append(-w)
# i = 0
# sum = 0
# while i < k-1:    
#     sum = q + w
#     my_list.append(sum)
#     my_list.append(-sum)
#     q = w
#     w = sum
#     i+=1
# my_list.sort()
# print(my_list)