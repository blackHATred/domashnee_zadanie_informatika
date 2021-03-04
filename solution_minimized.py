# -*- coding: utf-8 -*-
zadanie22, zadanie23, zadanie24, zadanie25, zadanie26, zadanie27 = lambda number: print(f'а) Количество цифр 3: {str(number).count("3")}\nб) Последняя цифра {str(number)[-1]} встречается {str(number).count(str(number)[-1])} раз(-а)\nв) Количество чётных цифр: {len([i for i in str(number) if int(i) % 2 == 0])}\nг) Сумма цифр, больших пяти: {sum([int(i) for i in str(number) if int(i) > 5])}\nд) Произведение цифр, больших семи: {8**str(number).count("8")*9**str(number).count("9")}\nе) Цифры от 0 до 5 встречаются {len([i for i in str(number) if int(i) < 6])} раз(-а)\n'), lambda number, a, x, y, z: print(f'а) Цифра {a} встречается {str(number).count(str(a))} раз(-а)\nб) Количество цифр, кратных {z}: {len([i for i in str(number) if int(i) % z == 0])}\nв) Сумма цифр, больших {a}: {len([i for i in str(number) if int(i) > a])}\nг) Цифры {x} и {y} встречаются {str(number).count(str(x)) + str(number).count(str(y))} раз(-а)'), lambda numbers, x: print(f'Сумма всех чисел, больших {x}: {sum([i for i in numbers if i > x])}\nКоличество чётных чисел последовательности: {len([i for i in numbers if i % 2 == 0])}'), lambda numbers: print(f'Знак меняется {len([i for i in range(i, len(numbers)) if (numbers[i] == abs(numbers[i]) and numbers[i-1] != abs(numbers[i-1])) or (numbers[i] != abs(numbers[i]) and numbers[i-1] == abs(numbers[i-1]))])} раз(-а)'), lambda n: print(f'а) Максимальная цифра - {max(str(n))}\nб) Минимальная цифра - {min(str(n))}'), lambda n: print(f'а) Максимальная цифра - {max(str(n))}, а минимальная цифра - {min(str(n))}\nб) Максимальная цифра больше минимальной на {int(max(str(n))) - int(min(str(n)))}\nв) Сумма минимальной и максимальной цифр - {sum([int(max(str(n))), int(min(str(n)))])}')
"""
zadanie22(number=int(input("Число n: ")))
zadanie23(number=int(input("Число n: ")),
          a=int(input("Число a: ")),
          x=int(input("Число x: ")),
          y=int(input("Число y: ")),
          z=int(input("Число z: ")))
zadanie24(numbers=list(map(int, input("Введите последовательность чисел: ").split())), x=int(input("Число x: ")))
zadanie25(numbers=tuple(map(int, input("Введите последовательность чисел: ").split())))
zadanie26(n=int(input("Введите натуральное число: ")))
zadanie27(n=int(input("Введие натуральное число: ")))
"""