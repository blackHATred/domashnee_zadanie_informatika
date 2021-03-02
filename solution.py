def z6_22(number: int) -> None:
    print(f'а) Количество цифр 3: {str(number).count("3")}')
    print(f'б) Последняя цифра {str(number)[-1]} встречается {str(number).count(str(number)[-1])} раз')
    print(f'в) Количество чётных цифр: {len([i for i in str(number) if int(i) % 2 == 0])}')
    print(f'г) Сумма цифр, больших пяти: {sum([int(i) for i in str(number) if int(i) > 5])}')
    print(f'д) Произведение цифр, больших семи: {8**str(number).count("8")*9**str(number).count("9")}')
    print(f'е) Цифры от 0 до 5 встречаются {len([i for i in str(number) if int(i) < 6])} раз')

def z6_23(number: int, a: int, x: int, y: int, z: int) -> None:
    print(f'а) Цифра {a} встречается {str(number).count(str(a))} раз')
    print(f'б) Количество цифр, кратных {z}: {len([i for i in str(number) if int(i) % z == 0])}')
    print(f'в) Сумма цифр, больших {a}: {len([i for i in str(number) if int(i) > a])}')
    print(f'г) Цифры {x} и {y} встречаются {str(number).count(str(x)) + str(number).count(str(y))} раз')

def z6_24(numbers: map, x: int) -> None:
    print(f'Сумма всех чисел, больших {x}: {sum([i for i in numbers if i > x])}')
    print(f'Количество чётных чисел последовательности: {len([i for i in numbers if i % 2 == 0])}')

def z6_25(numbers: tuple) -> None:
    print(f'Знак меняется {len([i for i in range(1, len(numbers)) if numbers[i] != abs(numbers[i]) and numbers[i-1] != abs(numbers[i-1])])} раз')

def z6_26(n: int) -> None:
    print(f'а) Максимальная цифра - {max(str(n))}\n б) Минимальная цифра - {min(str(n))}')

def z6_27(n: int) -> None:
    print(f'а) Максимальная цифра - {max(str(n))}, а минимальная цифра - {min(str(n))}')
    print(f'б) Максимальная цифра больше минимальной на {int(max(str(n))) - int(min(str(n)))}')
    print(f'в) Сумма минимальной и максимальной цифр - {sum([int(max(str(n))), int(min(str(n)))])}')

z6_22(number=int(input("Число n: ")))
z6_23(number=int(input("Число n: ")),
      a=int(input("Число a: ")),
      x=int(input("Число x: ")),
      y=int(input("Число y: ")),
      z=int(input("Число z: ")))
z6_24(numbers=map(int, input("Введите последовательность чисел: ").split()), x=int(input("Число x: ")))
z6_25(numbers=tuple(map(int, input("Введите последовательность чисел: "))))
z6_26(n=int(input("Введите натуральное число: ")))
z6_27(n=int(input("Введие натуральное число: ")))
