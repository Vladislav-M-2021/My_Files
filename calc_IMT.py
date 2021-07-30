"""
Расчет индекса массы тела
"""
# Ввести значения через пробел
w,r = map(float, input('Введите Вес(кг) и Рост(см) через пробел: ').split())

#w = int(input())  # Вес
#r = float(input())  # Рост

imt = w / (r / 100) ** 2  # Индекс массы тела
print(int(imt))

if imt < 18.5:
    print('Underweight')
if 18.5 <= imt < 25:
    print('Normal')
if 25.0 <= imt < 30:
    print('Overweight')
if imt >= 30:
    print('Obesity')
