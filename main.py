import random

# largest_number  = -999999999
# number = int(input("Введите число или напишите -1, чтобы остановить программу: "))
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Введите число или напишите -1, чтобы остановить программу: "))
# print("Наибольшее число из введённых: ", largest_number)

# pow = 1
# for exp in range(16):
#     print(f"2 в {exp} степени равно {pow}")
#     pow *= 2

# pow = 1
# for exp in range(1,16):
#     if exp >= 3:
#         # Прервать цикл
#         break
#     print(f"2 в {exp} степени равно {pow}")
#     pow *= 2

# #########################################
# # ИГРА Камень - Ножницы - Бумага - НАЧАЛО
# score_igroka = 0
# score_comp = 0
# cur_round = 0
# while cur_round < 3:
#     vyb_igroka = input("Введите (К-камень или Н-ножницы или Б-бумага): ")
#     if ((vyb_igroka == "К") or (vyb_igroka == "Н") or (vyb_igroka == "Б")):
#         vyb_comp = random.choice("КНБ")
#         cur_round = cur_round + 1
#     else:
#         print("Вы не ввели букву К или Н или Б")
#         continue
#     if (vyb_igroka == vyb_comp):
#         score_igroka = score_igroka + 1
#         score_comp = score_comp + 1
#         print(f"    {cur_round}-й раунд: ничья. Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "К") and (vyb_comp == "Н"):
#         score_igroka = score_igroka + 1
#         print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "К") and (vyb_comp == "Б"):
#         score_comp = score_comp + 1
#         print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "Н") and (vyb_comp == "К"):
#         score_comp = score_comp + 1
#         print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "Н") and (vyb_comp == "Б"):
#         score_igroka = score_igroka + 1
#         print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "Б") and (vyb_comp == "К"):
#         score_igroka = score_igroka + 1
#         print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
#     elif (vyb_igroka == "Б") and (vyb_comp == "Н"):
#         score_comp = score_comp + 1
#         print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")
#
# print("-------------------------------------------------------")
#
# if score_igroka > score_comp:
#     print(f"ИТОГО В ИГРЕ победил ИГРОК! Счёт {score_igroka}:{score_comp}")
# elif score_igroka < score_comp:
#     print(f"ИТОГО В ИГРЕ победил КОМПЬЮТЕР! Счёт {score_igroka}:{score_comp}")
# else:
#     print(f"ИТОГО В ИГРЕ победила ДРУЖБА! Счёт {score_igroka}:{score_comp}")
# # ИГРА Камень - Ножницы - Бумага - ОКОНЧАНИЕ
# #########################################

# #########################################
# # Задача с числом - НАЧАЛО
# vved_znach = str(input("Введите число: "))
# summa = 0 # Сумма всех цифр
# proizv = 1 # Произведение всех цифр
# col_zerro = 0 # Количество нулей
# sred = 0 # Среднее арифметическое
# col_nums = 0 # Количество цифр в числе
# for cur_num in vved_znach:
#     col_nums = col_nums + 1
#     summa = summa + int(cur_num)
#     proizv = proizv * int(cur_num)
#     if int(cur_num) == 0:
#         col_zerro = col_zerro + 1
#
# sred = summa / col_nums
# print(f"Сумма всех цифр числа {vved_znach} равна {summa}")
# print(f"Произведение всех цифр числа {vved_znach} равно {proizv}")
# print(f"Количество нулей в числе {vved_znach} равно {col_zerro}")
# print(f"Среднее арифметическое цифр в числе {vved_znach} равно {sred}")
#
# # Задача с числом - ОКОНЧАНИЕ
# #########################################

#########################################
# Шахматная доска - НАЧАЛО
razmer = int(input("Введите размер клетки: "))

for i in range(1, 9):
    for j in range(1, 5):
        if i % 2 == 0:
            symbol1 = "-"
            symbol2 = "*"
        else:
            symbol1 = "*"
            symbol2 = "-"
        for K in range(1, razmer + 1):
            for z in range(1, razmer + 1):
                print(symbol1, end=' ')
            for z in range(1, razmer + 1):
                print(symbol2, end=' ')
        print("")

# Шахматная доска - ОКОНЧАНИЕ
#########################################
