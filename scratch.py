# версия для слабовидящих
from random import randint

z_3 = lambda x: sorted(x)[-10]
z_4 = lambda x: sorted(x)[-6]
z_5 = lambda x, y: 'В классе X' if sorted(x)[-3] > sorted(y)[-3] else 'В классе Y'
z_6 = lambda x, y: 'В фирме X' if sorted(x)[-5] > sorted(y)[-5] else 'В фирме Y'
z_7 = lambda x: sorted(x)[4]
z_8 = lambda x: sorted(x)[4]
z_9 = lambda x, y: 'В классе X выше' if sorted(x)[-3] > sorted(y)[-3] else 'В классе Y выше'
z_10 = lambda x, y: 'В магазине X дороже' if sorted(x)[-4] > sorted(y)[-4] else 'В магазине Y дороже'
z_11 = lambda x: (sorted(x)[8] + sorted(x)[9])/2
z_12 = lambda x: (sorted(x)[6] + sorted(x)[7] + sorted(x)[8])/3
z_13 = lambda x: x.get(sorted(x)[3])
z_14 = lambda x: x.get(sorted(x)[5])
z_15 = lambda x, y: 'Списки из одинаковых фамилий' if set(x) == set(y) else 'Списки различаются'
z_16 = lambda x, y: 'Одинаковые наборы' if set(x) == set(y) else 'Разные наборы'
z_17 = lambda x: [int(''.join(sorted(str(x)))[::-1]), int(''.join(sorted(str(x))))]
z_18 = lambda x, y: 'Из одних цифр' if set(str(x)) == set(str(y)) else 'Из разных цифр'


print(z_3([randint(120, 220) for _ in range(25)]))
print(z_4([randint(200, 400) for _ in range(15)]))
print(z_5([randint(2, 5) for _ in range(18)], [randint(2, 5) for _ in range(18)]))
print(z_6([randint(10000, 50000) for _ in range(15)], [randint(10000, 50000) for _ in range(15)]))
print(z_7([randint(10000, 100000) for _ in range(12)]))
print(z_8([randint(1, 100) for _ in range(20)]))
print(z_9([randint(120, 220) for _ in range(23)], [randint(120, 220) for _ in range(23)]))
print(z_10([randint(10000, 50000) for _ in range(10)], [randint(10000, 50000) for _ in range(10)]))
print(z_11([randint(120, 220) for _ in range(18)]))
print(z_12([randint(120, 220) for _ in range(15)]))
print(z_13(dict([ (randint(100000, 5000000), f'Марка {i}') for i in range(7) ])))
print(z_14(dict([ (randint(120, 220), f'Фамилия {i}') for i in range(11) ])))
print(z_15([f'Фамилия {randint(0, 9)}' for _ in range(10)], [f'Фамилия {randint(0, 9)}' for _ in range(10)]))
print(z_16([f'Слово {randint(0, 11)}' for _ in range(12)], [f'Слово {randint(0, 11)}' for _ in range(12)]))
print(z_17(randint(100, 1000000)))
print(z_18(randint(10000, 99999), randint(10000, 99999)))
