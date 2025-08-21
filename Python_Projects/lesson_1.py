# Объявляем переменные разных типов
greeting = "Привет, студент!" # Это строка
name = "Иван" # Тоже строка
age = 30 # Целое число
temperature = 36.6 # Число с плавающей точкой
is_student = True # Логическое значение

# Выводим значение переменных на экран
print(greeting)
print("Меня зовут", name)
print("Мне", age, "лет")
print("Температура тела", temperature)
print("Я студент?", is_student)

# Проводим простые операции с числами
a = 15
b = 7
sum_result = a + b
diff_result = a - b

print("a + b =", sum_result)
print("a - b =", diff_result)

# Сложение строк
full_greeting = greeting + "" + name + "!"
print((full_greeting))

name = "Катерина"
city = "Лондоне"
age = "105"

print("Меня зовут", name)
print("Я живу в", city)
print("Мне", age, "лет")

days = 5
hours = days * 24

print("Сколько часов в", days, "днях?")
print(hours)