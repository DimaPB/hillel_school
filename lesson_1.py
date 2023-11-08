#1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
Num1 = 8
Num2 = 4

print(Num1+Num2)
print(Num1-Num2)
print(Num1*Num2)
print(type(Num1//Num2), Num1/Num2)
print(type(Num1/Num2), Num1//Num2)
# Решил использовать как / так и //


# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.

Num1 = int(input("Введіть перше число: "))
Num2 = int(input("Введіть друге число: "))

result = Num1/Num2
print(result)

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.

Num1 = int(input("Введіть перше число: "))
Num2 = int(input("Введіть друге число: "))

result = Num1//Num2
print(result)

# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.

Number = input("Введіть число: ")
print(type(int(Number)), Number)

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.


Num1 = (input("Введіть перше число: "))
Num2 = (input("Введіть друге число: "))

print(int(Num1)+int(Num2))
print(Num1+Num2)

# # 6 Вік користувача:
# # Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# # та вивести на екран два прінти: ім'я та скільки років користувачу.

Name = input("Enter your name: ")
Current_year = int(input("Enter current year: "))
Birthday_year = int(input("Enter your birth year: "))
age = Current_year - Birthday_year

print(Name, str(age) + " Years old")

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.
#
celsius = float(input("Enter the celsius: "))
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)


# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.
#
fahrenheit = float(input("Enter the celsius: "))
celsius = ((fahrenheit-32)*5)/9

print(celsius)


# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)


a = int(input("Enter the a: "))
b = a
c = ((a**2 + b**2))**(1/2)

print(c)

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

n = int(input("Enter the number of students: "))
assert n > 0 and n <= 10000 and n != float
k = int(input("Enter the number of apples: "))
assert 0 < k <= 10000 and k != float   # simplified variant of assert n > 0 and n <= 10000 and n != float

apples_for_student = k//n
basket = k % n

print("Number of apples for each student: ", apples_for_student)
print("Numbers of apples in the basket: ", basket)


# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.

pencils = int(input("Enter the number of pencils: "))
assert pencils <= 109
pens = int(input("Enter the number of pens: "))
assert pens <= 109
f_pens = int(input("Enter the number of f_pens : "))
assert f_pens <= 109

pencil_cost = 3
pen_cost = pencil_cost + 2 # 5
f_pen_cost = pen_cost + 7 # 12

cost_for_all = (pencils * pencil_cost) + (pens * pen_cost) + (f_pens * f_pen_cost)
print("Final price is: ", cost_for_all)


# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1


time = 0
time_in_minutes = int(input("Enter minutes: "))
# hours = time_in_minutes <= 24, time_in_minutes // 60 or time_in_minutes > 24, time_in_minutes - time_in_minutes
hours = time_in_minutes // 60
minutes = time_in_minutes % 60

hours = hours % 24
print(hours, minutes)


# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).

all_amount = int(input("Enter the amount of cranes: "))

Kate = Piter = Sergio = all_amount
Piter = Sergio = float(all_amount/6)
Kate = float((4*all_amount)/6)

print (Piter, Sergio, Kate)
# new coment


# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба сплатити податків за 3 місяці. Не забудьте ЄСВ(4422)


salary = float(input("Enter your salary: "))
salary = salary * 3

tax = 5 / 100
taxes = tax * salary

taxes_to_pay = taxes + 4422
print(taxes_to_pay)
