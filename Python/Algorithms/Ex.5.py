# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:39:55 2021

@author: User
"""

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

while True:
    try:
        n = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
prof_c = collections.deque()
unprof_c = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        prof_c.append(i)
    else:
        unprof_c.append(i)
print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')
for name in unprof_c:
    print(name)