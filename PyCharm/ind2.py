#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(float, input("Введите список --> ").split()))
    c = float(input('Введите c: '))
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    # Вывод меньших элементов
    s = 0
    for i in a:
        if i < c:
            s += 1
    print("Количество элементов списка, меньших с --> ", s)
    # Сумма отрицательных элементов
    n_0 = len(a)
    for i, item in reversed(list(enumerate(a))):
        if item < 0:
            n_0 = i
            break
    print("Сумма после отрицательного элемента --> ", sum([z for z in a[n_0+1:]]))
    # Сортировка элементов (от большего к меньшему)
    f = str(sorted(a, key=lambda x: abs(x-max(a))))
    print(f"Упорядоченный список: {f}")