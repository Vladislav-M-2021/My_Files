#year = int(input()
year = 1996

l1 = 'Leap year'
l2 = 'Not a leap year'

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(l1)
		else:
			print(l2)
	else:
		print(l1)
else:
	print(l2)


if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # A*(no_B+C) НЕ ПОНЯТНА АЛГЕБРА ЛОГИКИ!!!!!
    print('Leap year')
else:
    print('Not a leap year')

if year % 4 == 0 and year % 400 == 0:  # Эксперимент НЕУДАЧНЫЙ
    print('Leap year')
else:
    print('Not a leap year')
