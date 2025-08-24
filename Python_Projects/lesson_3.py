fruits = ['яблоко', 'банан', 'апельсин']

for fruit in fruits:  # Для каждого фрукта в списке fruits
    print(f"Я съел {fruit}")  # Выполнить этот код


# Повторить 5 раз
for i in range(5):
    print(f"Это повторение номер {i}")

counter = 5

while counter > 0:  # Пока counter больше 0
    print(f"Осталось итераций: {counter}")
    counter = counter - 1  # Уменьшаем counter на 1

for number in range(10):
    if number == 3:
        continue  # Пропустить число 3
    if number == 7:
        break  # Прервать цикл на числе 7
    print(number)

numbers = [9, 8, 1, 5, 11]

print("Число / Квадрат")
print("-----------")
for num in numbers:
    square = num * num
    print(f"{num:5} / {square:1}")

grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5]

print("Анализ оценок студентов:")
print("=" * 25)

for grade in grades:
    if grade >=3:
        print(f"Оценка: {grade} - сдал")
    else:
        print(f"Оценка: {grade} - не сдал")

temperature = [25, 18, -5, 30, 15, -2, 20]

print("Анализ температуры:")
print("=" * 25)

for temp in temperature:
    if temp >25:
        print(f"Температура: {temp}°C - жарко")
    elif temp >=10:
        print(f"Температура: {temp}°C - нормально")
    else:
        print(f"Температура: {temp}°C - холодно")

count = 10
print("Обратный отcчёт:")
print ("=" * 25)

while count > 0:
    print(f"Осталось секунд до запуска: {count}")
    count = count - 1

print ("Пуск!")

number = 1

while number <= 1000:
    print(f"Число: {number}")
    number = number * 2

print("Вводите числа. Для выхода введите 0")

while True:
    user_input = input("Введите число: ")
    number = int(user_input)

    if number == 0:
        print("Выход из программы...")
        break
    elif number < 0:
        print("Отрицательное число пропущено")
        continue
    else:
        square = number * number
        print(f"Квадрат числа {number} = {square}")