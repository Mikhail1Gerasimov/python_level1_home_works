﻿
__author__ = 'Герасимов Михаил Сергеевич'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

a = int(input ("Введите произвольное целое число: ")) # int нужен на случай ввода лидирующих нулей
a = str(a)
if int(a) >= 0:
    i = 0
    while i < len(a):
        print(a[i])
        i += 1
else:
    i = 1 # чтобы минус не выводить, если ввели отрицательное число
    while i < len(a):
        print(a[i])
        i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input ("Введите произвольное значение a: ")
b = input ("Введите произвольное значение b: ")

print("до:",a,b)
b1 = b

b = a
a = b1
print("после:",a,b)




# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a = input ("Сколько Вам полных лет: ")
if int(a) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')