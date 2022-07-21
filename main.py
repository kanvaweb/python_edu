
largest_number  = -999999999
number = int(input("Введите число или напишите -1, чтобы остановить программу: "))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Введите число или напишите -1, чтобы остановить программу: "))
print("Наибольшее число из введённых: ", largest_number)

pow = 1
for exp ing range(16):
    print(f"2 в {exp} степени равно {pow}")
    pow *= 2