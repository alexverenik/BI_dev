# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:01:08 2021

@author: User
"""

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

equation = input('Введите пример или 0 для выхода:\n')
while equation != '0':
    eq = list(equation.split())
    a = float(eq[0])
    b = float(eq[2])
    answer = "нет решения"
    if eq[1] == '+':
        answer = a + b
    elif eq[1] == '-':
        answer = a - b
    elif eq[1] == '*':
        answer = a * b
    elif eq[1] == '/':
        if b != 0:
            answer = a / b
        else:
            print('На ноль делить нельзя')
    else:
        print('Неверный формат ввода')
    print(f'{equation} = {answer}')
    equation = input('Введите пример или 0 для выхода:\n')
print('До свидания')


# 2. Посчитать четные и нечетные цифры введенного натурального числа.

number = input('Введите целое число: ')
odd = 0
even = 0
for num in number:
    if int(num) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В числе {number}: {odd} нечетных и {even} четных цифр')


4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
Количество элементов (n) вводится с клавиатуры.

length = int(input('Введите длину последовательности: '))
summa = 0
for i in range(length):
    summa += 1 / (-2) ** i
print(f'Сумма последовательности = {summa}')


# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random

number = random.randint(0, 101)
for i in range(10):
    num = int(input('Угадайте целое число от 0 до 100: '))
    if num == number:
        print('Поздравляем, вы угадали!')
        break
    elif num < number:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
print(f'Было загадано число {number}')







































