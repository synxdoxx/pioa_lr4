import re
import random

def read_set(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        elements = re.split(r'\s+', text.strip())
        return set(elements)

def union_sets(a, b):
    return a | b

def intersect_sets(a, b):
    return a & b

def subtract_sets(a, b):
    return a - b

def cartesian_product(a, b):
    result = set()
    for x in a:
        for y in b:
            result.add((x, y))
    return result

def selection_even(a, b):
    ev_a = set()
    ev_b = set()
    for el in a:
        if el.isdigit():
            if int(el) % 2 == 0:
                ev_a.add(el)
    for el in b:
        if el.isdigit():
            if int(el) % 2 == 0:
                ev_b.add(el)
    return ev_a, ev_b

def selection_odd(a, b):
    ev_a = set()
    ev_b = set()
    for el in a:
        if el.isdigit():
            if int(el) % 2 != 0:
                ev_a.add(el)
    for el in b:
        if el.isdigit():
            if int(el) % 2 != 0:
                ev_b.add(el)
    return ev_a, ev_b

def selection_random(a, b, k):
    if k <= len(a) and k<= len(b):
        rand_a = set(random.sample(sorted(a), k))
        rand_b = set(random.sample(sorted(b), k))
        return rand_a, rand_b
    else:
        return False

def projection(a, b):
    tuple1 = tuple(a)
    tuple2 = tuple(b)
    if len(tuple1) > len(tuple2):
        tuple2 += (0,) * (len(tuple1) - len(tuple2))
    elif len(tuple2) > len(tuple1):
        tuple1 += (0,) * (len(tuple2) - len(tuple1))

    data = set(zip(tuple1, tuple2))
    print(data)
    result = set()
    for row in data:
        result.add(row[0])
    return result

def join_sets(a, b):
    print(a, b)
    result = set()
    for l in a:
        for r in b:
            if l and r  and l[-1] == r[0]:
                result.add(l + r[1:])
    return result

def division_sets(a, b):
    if not b:
        return set()

    result = set()
    for x in a:
        if x in b:
            result.add(x)
    return result

def set_calculator(file1, file2):
    set_a = read_set(file1)
    set_b = read_set(file2)
    print(set_a, set_b)
    while True:
        print("Математичсекие операции")
        print("1. Объединение")
        print("2. Пересечение")
        print("3. Разность")
        print("4. Декартово произведение")
        print("5. Выборка четных")
        print("6. Выборка нечетных")
        print("7. Рандомная выборка")
        print("8. Проекция")
        print("9. Соединение")
        print("10. Деление")
        print("0. Выход")

        choice = input("Выберите операцию: ").strip()

        if choice == '0':
           print("Выход")
           break

        # 1. ОБЪЕДИНЕНИЕ
        if choice == '1':
           result = union_sets(set_a, set_b)
           print("Результат:", result)

        # 2. ПЕРЕСЕЧЕНИЕ
        elif choice == '2':
           result = intersect_sets(set_a, set_b)
           print("Результат:", result)

        # 3. РАЗНОСТЬ
        elif choice == '3':
           result = subtract_sets(set_a, set_b)
           print("Результат:", result)

        # 4. ДЕКАРТОВО ПРОИЗВЕДЕНИЕ
        elif choice == '4':
            result = cartesian_product(set_a, set_b)
            print("Результат:", result)

        # 5. ВЫБОРКА ЧЕТНЫХ
        elif choice == '5':
            result = selection_even(set_a, set_b)
            print("Результат:", result)

        # 6. ВЫБОРКА НЕЧЕТНЫХ
        elif choice == '6':
            result = selection_odd(set_a, set_b)
            print("Результат:", result)

        # 7. ВЫБОРКА РАНДОМНЫХ
        elif choice == '7':
            while True:
                k = int(input('Сколько чисел выбрать? '))
                result = selection_random(set_a, set_b, k)
                if result != False:
                    break
            print("Результат:", result)

        # 8. ПРОЕКЦИЯ (по первому элементу)
        elif choice == '8':
            result = projection(set_a, set_b)
            print("Результат:", result)

        # 9. СОЕДИНЕНИЕ
        elif choice == '9':
            result = join_sets(set_a, set_b)
            print("Результат:", result)

        # 10. ДЕЛЕНИЕ
        elif choice == '10':
            result = division_sets(set_a, set_b)
            print("Результат:", result)

set_calculator('txt1', 'txt2')
