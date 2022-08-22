############################################
# Выбор параметров - НАЧАЛО
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
# Выбор параметров - ОКОНЧАНИЕ
############################################

def function1(diapazon_1, diapazon_2):
	# Пользователь должен ввести число делитель.
	# Программа должна вывести все числа в заданном диапазоне,
	# которые делятся на введенное число без остатка.

	delitel = int(input("Задание 1. Введите делитель: "))
	for i in range(diapazon_1, diapazon_2+1):
		if i % delitel == 0:
			print(f"    Число {i} делится на {delitel} без остатка")

def function2(diapazon_1, diapazon_2):
	# Перемножить все нечётные числа в указанном диапазоне
	mnoj = 1
	for i in range(diapazon_1, diapazon_2+1):
		if i % 2 != 0:
			mnoj = mnoj * i

	print(f"     Задание 2. Произведение всех нечётных чисел равно {mnoj}")

def function3(diapazon_1, diapazon_2):
	# Пользователь вводит число. Программа должна посчитать сколько раз встречается это число
	chislo = int(input("Задание 3. Введите число для поиска: "))
	kolvo = 0
	for i in range(diapazon_1, diapazon_2+1):
		if i == chislo:
			kolvo = kolvo + 1

	print(f"    Число {chislo} встречается в диапазоне {kolvo} раз")



def function4(diapazon_1, diapazon_2):
	# Перевод из арабские числа в римские от 1 до 10000 введённого диапазона
	def poluchit_desyatoe(curr_num):
		if curr_num == 1:
			return "I"
		elif curr_num == 2:
			return "II"
		elif curr_num == 3:
			return "III"
		elif curr_num == 4:
			return "IV"
		elif curr_num == 5:
			return "V"
		elif curr_num == 6:
			return "VI"
		elif curr_num == 7:
			return "VII"
		elif curr_num == 8:
			return "VIII"
		elif curr_num == 9:
			return "IX"
		elif curr_num == 10:
			return "X"
		elif curr_num == 0:
			return ""

	def poluchit_sotoe(curr_num):
		sotaya = ""
		if curr_num == 100:
			return "C"
		elif curr_num == 1000:
			return "M"
		elif (curr_num >= 10) and (curr_num <= 19):
			sotaya = "X"
		elif (curr_num >= 20) and (curr_num <= 29):
			sotaya = "XX"
		elif (curr_num >= 30) and (curr_num <= 39):
			sotaya = "XXX"
		elif (curr_num >= 40) and (curr_num <= 49):
			sotaya = "XL"
		elif (curr_num >= 50) and (curr_num <= 59):
			sotaya = "L"
		elif (curr_num >= 60) and (curr_num <= 69):
			sotaya = "LX"
		elif (curr_num >= 70) and (curr_num <= 79):
			sotaya = "LXX"
		elif (curr_num >= 80) and (curr_num <= 89):
			sotaya = "LXXX"
		elif (curr_num >= 90) and (curr_num <= 99):
			sotaya = "XC"

		lev = str(curr_num)[0:1]
		prav = str(curr_num)[1:2]
		# print(f"prav = {prav}")
		sotaya = sotaya + poluchit_desyatoe(int(prav))
		# print(f"sotaya = {sotaya}")
		return sotaya

	def poluchit_tysyachnoe(curr_num):
		lev = int(str(curr_num)[0:1])
		sred = str(curr_num)[1:3]
		# prav = str(curr_num)[2:3]
		# print(f"sred тысячное = {sred}")

		tysyachnoe = ""
		if (lev == 1):
			tysyachnoe = "C"
		elif (lev == 2):
			tysyachnoe = "CC"
		elif (lev == 3):
			tysyachnoe = "CCC"
		elif (lev == 4):
			tysyachnoe = "CD"
		elif (lev == 5):
			tysyachnoe = "D"
		elif (lev == 6):
			tysyachnoe = "DC"
		elif (lev == 7):
			tysyachnoe = "DCC"
		elif (lev == 8):
			tysyachnoe = "DCCC"
		elif (lev == 9):
			tysyachnoe = "CM"

		if int(sred) <= 9:
			tysyachnoe = tysyachnoe + poluchit_desyatoe(int(sred))
		else:
			tysyachnoe = tysyachnoe + poluchit_sotoe(int(sred))
		return tysyachnoe

	def poluchit_desyati_tysyachnoe(curr_num):
		lev = int(str(curr_num)[0:1])
		sred = str(curr_num)[1:4]
		# print(f"   десятитысячное  lev = {lev},  sred= {sred}")

		desyati_tysyachnoe = ""
		if (lev == 1):
			desyati_tysyachnoe = "M"
		elif (lev == 2):
			desyati_tysyachnoe = "MM"
		elif (lev == 3):
			desyati_tysyachnoe = "MMM"
		elif (lev == 4):
			desyati_tysyachnoe = "Mv"
		elif (lev == 5):
			desyati_tysyachnoe = "v"
		elif (lev == 6):
			desyati_tysyachnoe = "vM"
		elif (lev == 7):
			desyati_tysyachnoe = "vMM"
		elif (lev == 8):
			desyati_tysyachnoe = "vMMM"
		elif (lev == 9):
			desyati_tysyachnoe = "vMv"

		if int(sred) <= 9:
			desyati_tysyachnoe = desyati_tysyachnoe + poluchit_desyatoe(int(sred))
		elif (int(sred) >= 10) and (int(sred) <= 99):
			desyati_tysyachnoe = desyati_tysyachnoe + poluchit_sotoe(int(sred))
		else:
			desyati_tysyachnoe = desyati_tysyachnoe + poluchit_tysyachnoe(int(sred))
		return desyati_tysyachnoe

	def poluchit_rimskoe(curr_num):
		if (curr_num >= 1) and (curr_num <= 10): # Получаем десятые доли в римской системе
			return poluchit_desyatoe(curr_num)
		elif (curr_num >= 11) and (curr_num <= 100):  # Получаем сотые доли в римской системе
			return poluchit_sotoe(curr_num)
		elif (curr_num >= 101) and (curr_num <= 999): # Получаем тысячные доли в римской системе
			return poluchit_tysyachnoe(curr_num)
		elif (curr_num >= 1000) and (curr_num <= 9999):  # Получаем десятитысячные доли в римской системе
			return poluchit_desyati_tysyachnoe(curr_num)

	for i in range(diapazon_1, diapazon_2+1):
		rimskoe = poluchit_rimskoe(i)
		print(f"    {i} = {rimskoe}")


if num_task == 1:
	function1(diapazon_1, diapazon_2)
elif num_task == 2:
	function2(diapazon_1, diapazon_2)
elif num_task == 3:
	function3(diapazon_1, diapazon_2)
elif num_task == 4:
	function4(diapazon_1, diapazon_2)
	print("Перевод в римскую систему счисления работает в диапазоне от 1 до 10000. (Маленькое v - это V с чертой сверху)")
else:
	print("Ошибка ввода. Обратитесь, пожалуйста, к разработчикам")