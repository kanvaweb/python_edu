import random

############################################
# 1. Домашнее задание - НАЧАЛО
chislo1 = int(input("Введите число 1: "))
chislo2 = int(input("Введите число 2: "))
chislo3 = int(input("Введите число 3: "))
summa_chisel = chislo1 + chislo2 + chislo3
proizv_chisel = chislo1 * chislo2 * chislo3
print(f"    {chislo1} + {chislo2} + {chislo3} = {summa_chisel}")
print(f"    {chislo1} * {chislo2} * {chislo3} = {proizv_chisel}")
# 1. Домашнее задание - ОКОНЧАНИЕ
############################################
print("")

############################################
# 2. Домашнее задание - НАЧАЛО
zarplata = float(input("Введите месячную зарплату (руб.): "))
kredit = float(input("Какой у Вас ежемесячный платеж по кредиту (руб.): "))
kommunalka = float(input("Введите задолженность за коммунальные услуги (руб.): "))
itogo_ostalos = zarplata - kredit - kommunalka
print(f"    Итого на месяц осталось ({zarplata} - {kredit} - {kommunalka}) = {itogo_ostalos} (руб.)")
# 2. Домашнее задание - ОКОНЧАНИЕ
############################################
print("")

############################################
# 3. Домашнее задание - НАЧАЛО
diagonal_romba1 = float(input("Введите длину первой диагонали ромба (см.): "))
diagonal_romba2 = float(input("Введите длину второй диагонали ромба (см.): "))
ploshad_romba = (diagonal_romba1 * diagonal_romba2) / 2
print(f"    Площадь ромба ({diagonal_romba1} * {diagonal_romba2}) / 2 =  {ploshad_romba} (см2.)")
# 3. Домашнее задание - ОКОНЧАНИЕ
############################################
print("")


############################################
# 4. Домашнее задание - НАЧАЛО
# Программа выводит строку "To be or not to be" построчно,
# случайно выбирая кол-во слов в каждой подстроке
stroka = "To be or not to be"
perv_probel = stroka.find(" ")
tek_slovo = ""
while perv_probel != -1:
	tek_slovo = tek_slovo + stroka[0:perv_probel] + " "
	sluch_chislo = int(random.random() * 2) # Получаем случайное число 0 или 1, если 0, то не выводим строку, а если 1 то выводим накопившуюся

	if sluch_chislo == 1:
		print(f"{tek_slovo}")
		tek_slovo = ""

	stroka = stroka[perv_probel + 1:]
	perv_probel = stroka.find(" ")
else:
	# После выполнения цикла выводим то, что не вывелось в цикле
	# и "хвостовую часть" строки (после последнего пробела)
	stroka = tek_slovo + stroka
	print(f"{stroka}")
# 4. Домашнее задание - ОКОНЧАНИЕ
############################################
print("")


############################################
# 5. Домашнее задание - НАЧАЛО
# Программа выводит строку "«Life is what happens when you're
# busy making other plans» John Lennon" построчно с увеличивающимся
# отступом, случайно выбирая кол-во слов в каждой подстроке
stroka = "«Life is what happens when you're busy making other plans» John Lennon"
perv_probel = stroka.find(" ")
tek_slovo = ""
nomer_stroki = 0
while perv_probel != -1:
	tek_slovo = tek_slovo + stroka[0:perv_probel] + " "
	sluch_chislo = int(random.random() * 2) # Получаем случайное число 0 или 1, если 0, то не выводим строку, а если 1 то выводим накопившуюся

	if sluch_chislo == 1:
		preprobel = "    " * nomer_stroki # Отступ по кол-ву строк
		tek_slovo = preprobel + tek_slovo
		print(f"{tek_slovo}")
		tek_slovo = ""
		nomer_stroki = nomer_stroki + 1

	stroka = stroka[perv_probel + 1:]
	perv_probel = stroka.find(" ")
else:
	# После выполнения цикла выводим то, что не вывелось в цикле
	# и "хвостовую часть" строки (после последнего пробела)
	preprobel = "    " * nomer_stroki  # Отступ по кол-ву строк
	stroka = preprobel + tek_slovo + stroka
	print(f"{stroka}")
# 5. Домашнее задание - ОКОНЧАНИЕ
############################################
