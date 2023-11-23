# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно)
# (так як робили на уроці).
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


# def return_table(operator: str):
#     table = {"+": [], "-": [], "*": [], "/": []}
#     for i in range(2, 10):
#         for j in range(2, 10):
#             table["+"].append(f"{i}+{j}={i+j}")
#             table["-"].append(f"{i}-{j}={i-j}")
#             table["*"].append(f"{i}*{j}={i*j}")
#             table["/"].append(f"{i}/{j}={round(i/j, 2)}")
#
#     return print(table[operator])
#
#
# return_table(operator=input("Select the operation: "))


# Задача 1
#
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
# якщо менше. то тоді просто відкидаємо копійки від ціни.


print("Enter the prices using spaces between them")
price = input("Enter the prices: ")
price = price.split()

the_sum = 0
for i in price:
    the_sum = the_sum + int(i)
the_sum = the_sum * (1 - 6.5/100)
discount = input("Do you have an discount? (yes/no): ").lower()
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
    the_sum += 1
    print(f"The sum is {the_sum.__round__(0)}")
else:
    print(f"The sum is {the_sum.__round__(0)}")