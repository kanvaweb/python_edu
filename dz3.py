def ubrat_chislo(str_cur, num_cur):
	# Функция ubrat_chislo (строка, удаляемое число) убирает все вхождения в строку удаляемого числа
	if str_cur == "," or str_cur == "":
		return ""
	str = ""
	for i in range(1, len(str_cur) + 1):
		first_num = str_cur[:str_cur.find(",")]
		str_cur = str_cur[str_cur.find(",")+1:]
		if (first_num != num_cur) and (first_num != ""):
			str = str + first_num + ","
	if str == "":
		str = num_cur + "," # Если это последнее число, то его полностью не удаляем

	# print(f"   ПОСЛЕ УДАЛЕНИЯ str = {str}")
	return str

def stroka_bez_delitel(str_cur, delitel, cur_index):
	# Функция stroka_bez_delitel (строка, кратное, текущий индекс) убирает первое число с начала строки,
	# но если это не расстреливаемый, то оставляет его дальше по строке,
	# если расстреливаемый, то удаляет по встрей строке
	if str_cur == "," or str_cur == "":
		return "" # если вдруг получили пустое значение в виде строки, то выходим
	first_num = str_cur[:str_cur.find(",")] # получаем первое число в строке
	last_num = str_cur[str_cur.find(",")+1:] # получаем строку без первого числа в строке
	print(f"first_num = {first_num}") # для отладки

	if cur_index % delitel == 0: # если это расстреливаемый, то удаляем его из всей строки
		last_num = ubrat_chislo(last_num, first_num) #Из строки last_num убрать все вхождения числа first_num

	return last_num

humans = int(input("Введите кол-во человек в круге: "))
# humans = 8 # для тестирования
if humans <= 0:
	print("! Кол-во человек не может быть отрицательным или = 0")
	exit()

delitel = int(input("Введите какой человек будет расстрелян: "))
# delitel = 3 # для тестирования
if delitel <= 0:
	print("! Расстреливаемый не может быть отрицательным или = 0")
	exit()

str_hum = ""
for i in range(1, humans + 1):
	str_hum = str_hum + str(i) + ","
str_hum = str_hum * (delitel + 100)  # делаем по сути бесконечную строку, имитация круга

# print(f"Первоначальная строка: {str_hum}")
print("!!!!!!!!!!!!!!!!!!!!!! НАЧАЛО ОТЛАДКИ !!!!!!!!!!!!!!!!!!!!!!")
vyzhivshyi = "Не найден"
index = 0
for i in range(humans * (delitel + 100)): # по сути выполняем бесконечный цикл, а как закончатся числа выйдем из цикла
	print(f"Итерация: {i+1} str_hum = {str_hum}")  # для отладки выводим номер шага
	index = index + 1
	str_hum = stroka_bez_delitel(str_hum, delitel, index)
	if index == delitel:
		print(f"            ^ меня удалить")  # для отладки понимать какое число будет удалено
		index = 0 # Обнуляем индекс
	if str_hum.count(",") == 1:
		vyzhivshyi = str_hum[:str_hum.find(",")]
		break
	if str_hum == "":
		break

print("!!!!!!!!!!!!!!!!!!!!!! ОКОНЧАНИЕ ОТЛАДКИ !!!!!!!!!!!!!!!!!!!!!!")
print(f"!!!   ВЫЖИВШИЙ найденный по строке = {vyzhivshyi}")


def lastSurvivor(humans, delitel):
	if humans == 1:
		return 1
	elif humans > 1:
		return (1 + (lastSurvivor(humans - 1, delitel) + delitel - 1) % humans)

Last_Survivor_Num = str(lastSurvivor(humans, delitel))
print(f"!!!   Проверяем РЕКУРСИВНО* = lastSurvivor({humans}, {delitel}) = {Last_Survivor_Num}  (* функция взята из интернета)")

if Last_Survivor_Num == vyzhivshyi:
	print(f"!!!   Результаты совпадают!")
else:
	print(f"!!!   НЕ СОВПАДАЮТ РЕЗУЛЬТАТЫ ФУНКЦИЙ !!!")

