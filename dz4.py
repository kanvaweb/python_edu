############################################
# Задание 4.1 - НАЧАЛО

# Есть некоторый текст. Реализуйте следующую функциональность:
#   1) Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
#           (Раздедлители предложений ".", "!", "?")
#   2) Посчитайте сколько раз цифры встречаются в тексте;
#   3) Посчитайте сколько раз знаки препинания встречаются в тексте;

def capitalize_m(my_str):

	if my_str == "":
		return ""

	cur_razd1 = "." # первый возможный разделитель "." точка
	str_razd1 = my_str.find(cur_razd1) # номер позиции "." или -1, если нет в строке
	cur_razd2 = "!" # второй возможный разделитель "!" восклицательный знак
	str_razd2 = my_str.find(cur_razd2) # номер позиции "!" или -1, если нет в строке
	cur_razd3 = "?" # третий возможный разделитель "?" вопросительный знак
	str_razd3 = my_str.find(cur_razd3) # номер позиции "?" или -1, если нет в строке

	if (str_razd1 == -1) and (str_razd2 == -1) and (str_razd3 == -1):
		# если разделителей не осталось, то возвращаем последнее предложение
		# без пробелов слева и справа и с заглавной буквы. Это последнее предложение в строке.
		return(my_str.strip().capitalize())
	elif (str_razd1 != -1) and (str_razd2 != -1) and (str_razd3 != -1): # если есть все 3 разделителя
		if (str_razd1 < str_razd2) and (str_razd1 < str_razd3):
			str_razd = str_razd1
			cur_razd = cur_razd1
		elif (str_razd2 < str_razd1) and (str_razd2 < str_razd3):
			str_razd = str_razd2
			cur_razd = cur_razd2
		else:
			str_razd = str_razd3
			cur_razd = cur_razd3
	elif (str_razd1 != -1) and (str_razd2 != -1) and (str_razd3 == -1): # если есть первый и второй
		if (str_razd1 < str_razd2):
			str_razd = str_razd1
			cur_razd = cur_razd1
		else:
			str_razd = str_razd2
			cur_razd = cur_razd2
	elif (str_razd1 != -1) and (str_razd2 == -1) and (str_razd3 != -1): # если есть первый и третий
		if (str_razd1 < str_razd3):
			str_razd = str_razd1
			cur_razd = cur_razd1
		else:
			str_razd = str_razd3
			cur_razd = cur_razd3

	elif (str_razd1 == -1) and (str_razd2 != -1) and (str_razd3 != -1): # если есть второй и третий
		if (str_razd2 < str_razd3):
			str_razd = str_razd2
			cur_razd = cur_razd2
		else:
			str_razd = str_razd3
			cur_razd = cur_razd3
	elif (str_razd1 != -1) and (str_razd2 == -1) and (str_razd3 == -1): # если только первый
		str_razd = str_razd1
		cur_razd = cur_razd1
	elif (str_razd1 == -1) and (str_razd2 != -1) and (str_razd3 == -1): # если только второй
		str_razd = str_razd2
		cur_razd = cur_razd2
	elif (str_razd1 == -1) and (str_razd2 == -1) and (str_razd3 != -1): # если только третий
		str_razd = str_razd3
		cur_razd = cur_razd3

	# print(f'!!! my_str: "{my_str}"  .={str_razd1}  !={str_razd2}  ?={str_razd3}  min={str_razd}')

	# функция возвращает первое предложение с присоединённым к нему
	# первым предложением следующего предложения и так далее до конца строки
	return my_str[0:str_razd].capitalize() + cur_razd + " " + capitalize_m(my_str[str_razd+1:].strip().capitalize())

# nekiy_text = str(input("Введите, пожалуйста, некоторый текст: "))
nekiy_text = "привет, 23-ий! приветствую! как дела у 657? нормально как и у 55." # для отладки алгоритма

print(f'ПЕРВОНАЧАЛЬНЫЙ ТЕКСТ: "{nekiy_text}"')

capit = capitalize_m(nekiy_text).strip()  # рекурсивная функция
print(f'Задание 1: Предложения с заглавной буквы: "{capit}"')
# Задание 4.1 - ОКОНЧАНИЕ


# Задание 4.2 - НАЧАЛО
# Посчитайте сколько раз цифры встречаются в тексте

skolko_cifr_itogo = 0
for i in range(0,10):
	skolko_cifr_itogo = skolko_cifr_itogo + nekiy_text.count(str(i))

print(f'Задание 2: В предложении всего "{skolko_cifr_itogo}" цифр')

# Задание 4.2 - ОКОНЧАНИЕ


# Задание 4.3 - НАЧАЛО
# Посчитайте сколько раз знаки препинания встречаются в тексте

skolko_znakov_itogo = 0
vse_znaki = "':,-.!?;"

for i in vse_znaki:
	skolko_znakov_itogo = skolko_znakov_itogo + nekiy_text.count(i)

print(f'Задание 3: В предложении всего "{skolko_znakov_itogo}" знаков препинания')

# Задание 4.3 - ОКОНЧАНИЕ
