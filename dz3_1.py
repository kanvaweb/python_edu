############################################
# 1. Домашнее задание - НАЧАЛО
diapazon_1 = int(input("Введите начальное целое число диапазона: "))
diapazon_2 = int(input("Введите конечное целое число диапазона: "))
if diapazon_2 < diapazon_1: # Если конечное число диапазона меньше начального поменяем их местами без доп. переменных
	diapazon_1 = diapazon_1 + diapazon_2
	diapazon_2 = diapazon_1 - diapazon_2
	diapazon_1 = diapazon_1 - diapazon_2

num_task = 0
while (num_task < 1) or (num_task > 4):
	num_task = int(input("Введите какое задание выполнить 1, 2, 3 или 4: "))
	if (num_task < 1) or (num_task > 4):
		print("    Вы ввели число не от 1 до 4 включительно. Попробуйте ещё раз и у Вас получится!")
# print(f"    {chislo1} ** {chislo2} = {stepen_chisla}")
############################################
