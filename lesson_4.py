# Задача 1
#
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
# якщо менше. то тоді просто відкидаємо копійки від ціни.

import decimal
print("Enter the prices using spaces between them")
price = input("Enter the prices: ")
price = price.split()

the_sum = 0
for i in price:
    the_sum = the_sum + int(i)
    # i += i не понимаю почему тут с і ничего не надо делать, оно само берет следущее значение в массиве
the_sum = the_sum * (1 - 6.5/100)
discount = input("Do you have an discount? ").lower()
if discount == "yes":
    type_of_discount = input("Which one do ypu have? sum or %? ").lower()
    if type_of_discount == "sum":
        discount_amount = int(input("Enter your discount "))
        the_sum = the_sum - discount_amount
    elif type_of_discount == "%":
        discount_amount = float(input("Enter your discount "))
        the_sum = the_sum * (1 - discount_amount/100)
    else:
        print("Incorrect type of discount")
rounded_sum = the_sum.__round__(0)
if the_sum - rounded_sum >= 0.44:
    the_sum =+ 1
    print(f"The sum is {the_sum.__round__(0)}")
else:
    print(f"The sum is {the_sum.__round__(0)}")

# Задача 2
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in.
#
# Задача  3
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.

PIN = 1234
i = 0
while i < 3:
    pin_check = int(input("Enter your pin code: "))
    i += 1
    if pin_check == PIN:
        print("Pin is correct")
        break

    elif i < 3:
        continue
    else:
        print("Your card is blocked")

#
# Задача 4
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг  | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)

