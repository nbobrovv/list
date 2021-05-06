#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = list(map(int, input("Введите список --> ").split()))
    c = int(input('Введите c: '))
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
    print("Сумма после отрицательного элеммента --> ",
          str(sum(map(int, a[max(enumerate(a), key=lambda ix: (ix[1] < 0, ix[0]))[0] + 1:]))))
    # Сортировка элементов (от большего к меньшему)
    f = str(sorted(a, key=lambda x: abs(x-max(a))))
    print(f"Упорядоченный список: {f}")