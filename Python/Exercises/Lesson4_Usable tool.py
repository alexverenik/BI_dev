


"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами."""


from sys import argv
from Function_salary import count_salary 

file, input_in_hours, rate_of_pay, bonus = argv

print(count_salary (int(input_in_hours), int(rate_of_pay), int(bonus)))


"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [my_list[el] for el in range (1, len(my_list)) if my_list[el] > my_list[el-1]]
print(new_list)



"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор."""

my_list = [el for el in range (20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)



"""4. Представлен список чисел. Определите элементы списка, не имеющие повторений. 
Сформируйте итоговый массив чисел, соответствующих требованию. 
Элементы выведите в порядке их следования в исходном списке. 
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)

new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)



"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти чётные числа от 100 до 1000 (включая границы). 
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

my_list = [el for el in range (100, 1001) if el % 2 == 0]
print(my_list)

multiplying = reduce((lambda x, y: x * y), my_list)
print(multiplying)



"""6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения. 
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится."""

from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)



"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). 
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

n = int(input("Enter n: "))


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        yield f


g = fact(n)
print(g)
for el in g:
    print(el)






































