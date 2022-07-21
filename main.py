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

score_igroka = 0
score_comp = 0
cur_round = 0
while cur_round < 3:
    vyb_igroka = input("Введите (К-камень или Н-ножницы или Б-бумага): ")
    if ((vyb_igroka == "К") or (vyb_igroka == "Н") or (vyb_igroka == "Б")):
        vyb_comp = random.choice("КНБ")
        cur_round = cur_round + 1
    else:
        print("Вы не ввели букву К или Н или Б")
        continue
    if (vyb_igroka == vyb_comp):
        score_igroka = score_igroka + 1
        score_comp = score_comp + 1
        print(f"    {cur_round}-й раунд: ничья. Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "К") and (vyb_comp == "Н"):
        score_igroka = score_igroka + 1
        print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "К") and (vyb_comp == "Б"):
        score_comp = score_comp + 1
        print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "Н") and (vyb_comp == "К"):
        score_comp = score_comp + 1
        print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "Н") and (vyb_comp == "Б"):
        score_igroka = score_igroka + 1
        print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "Б") and (vyb_comp == "К"):
        score_igroka = score_igroka + 1
        print(f"    {cur_round}-й раунд: победа игрока.  Компьютер выбрал \"{vyb_comp}\"")
    elif (vyb_igroka == "Б") and (vyb_comp == "Н"):
        score_comp = score_comp + 1
        print(f"    {cur_round}-й раунд: победа компьютера.  Компьютер выбрал \"{vyb_comp}\"")

print("-------------------------------------------------------")

if score_igroka > score_comp:
    print(f"ИТОГО В ИГРЕ победил ИГРОК! Счёт {score_igroka}:{score_comp}")
elif score_igroka < score_comp:
    print(f"ИТОГО В ИГРЕ победил КОМПЬЮТЕР! Счёт {score_igroka}:{score_comp}")
else:
    print(f"ИТОГО В ИГРЕ победила ДРУЖБА! Счёт {score_igroka}:{score_comp}")

