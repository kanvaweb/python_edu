############################################
# 1. Домашнее задание - НАЧАЛО
print("Задание № 1:")
chislo1 = int(input("1. Введите целое число 1: "))
chislo2 = int(input("2. Введите целое число 2: "))
stepen_chisla = chislo1 ** chislo2
print(f"    {chislo1} ** {chislo2} = {stepen_chisla}")
print("")
# 1. Домашнее задание - ОКОНЧАНИЕ
############################################

############################################
# 2. Домашнее задание - НАЧАЛО
print("Задание № 2:")
num1 = 100 # Начальное число
num2 = 999 # Конечное число
count_double = 0 # Кол-во чисел, у которых есть 2 одинаковых цифры
for num_curr in range(num1, num2 + 1):
	str_curr = str(num_curr)
	if ((str_curr[0] == str_curr[1]) and (str_curr[0] != str_curr[2])) or ((str_curr[0] == str_curr[2]) and (str_curr[0] != str_curr[1])) or ((str_curr[1] == str_curr[2]) and (str_curr[0] != str_curr[2])):
		count_double = count_double + 1
		if count_double % 10 == 0:
			print(f"{num_curr}, ")  # после вывода 10 чисел перенос строки
		else:
			print(f"{num_curr}, ", end = " ")

print("")
print(f"      Кол-во чисел только с двумя одинаковыми цифрами: {count_double}")
print("")
# 2. Домашнее задание - ОКОНЧАНИЕ
############################################

# ############################################
# 3. Домашнее задание - НАЧАЛО
print("Задание № 3:")
num1 = 100 # Начальное число
num2 = 9999 # Конечное число
count_vse_razn = 0 # Кол-во чисел, у которых все цифры разные
for num_curr in range(num1, num2 + 1):
	str_curr = str(num_curr)
	cur_razn = 0 # 0-если в текущем числе все одинаковые; 1 - если все разные
	if num_curr <= 999:
		if (str_curr[0] != str_curr[1]) and (str_curr[0] != str_curr[2]) and (str_curr[1] != str_curr[2]):
			cur_razn = 1
	else:
		if (str_curr[0] != str_curr[1]) and (str_curr[0] != str_curr[2]) and (str_curr[0] != str_curr[3]) and (str_curr[1] != str_curr[2]) and (str_curr[1] != str_curr[3]) and (str_curr[2] != str_curr[3]):
			cur_razn = 1

	if cur_razn == 1:
		count_vse_razn = count_vse_razn + 1
		if count_vse_razn % 10 == 0: # после вывода 10 чисел перенос строки
			print(f"{num_curr}, ")
		else:
			print(f"{num_curr}, ", end = " ")

print("")
print(f"      Кол-во чисел со всеми разными цифрами: {count_vse_razn}")
print("")
# 3. Домашнее задание - ОКОНЧАНИЕ
############################################


############################################
# 4. Домашнее задание - НАЧАЛО
# Пользователь вводит любое целое число. Необходимо из этого
# целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
print("Задание № 4:")
chislo_str = str(input("Введите целое число: "))
chislo_bez36 = ""
for curr_char in chislo_str:
	if (curr_char != "3") and (curr_char != "6"):
		chislo_bez36 = chislo_bez36 + curr_char

print(f"Число без цифр 3 и 6: {chislo_bez36}")
print("")
# 4. Домашнее задание - ОКОНЧАНИЕ
############################################
