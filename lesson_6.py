# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно)
# (так як робили на уроці).
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


def return_table(operator: str):
    table = {"+": [], "-": [], "*": [], "/": []}
    for i in range(2, 10):
        for j in range(2, 10):
            table["+"].append(f"{i}+{j}={i+j}")
            table["-"].append(f"{i}-{j}={i-j}")
            table["*"].append(f"{i}*{j}={i*j}")
            table["/"].append(f"{i}/{j}={round(i/j, 2)}")

    print((table[operator]))


return_table(operator=input("Select the operation: "))


# Задача 1
#
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
# якщо менше. то тоді просто відкидаємо копійки від ціни.

def return_price():
    prices = input("Enter the prices using spaces between them: ")
    return prices


def return_having():
    discount = input("Do you have an discount? (yes/no): ").lower()
    return discount


def discount_type():
    disc_type = input("Which one do ypu have? sum or %? ").lower()
    return disc_type


def discount_amount(type_of_discount, price):
    if type_of_discount == "sum" or type_of_discount == "%":
        amount = int(input("Enter your discount: "))
        if type_of_discount == "sum":
            result = price - amount
            print(round(result, 2))
            return result
        else:
            result = price * (1 - amount/100)
            print(round(result, 2))
            return result
    else:
        print("Incorrect type of discount")


def rounding(resultat):
    rounded_sum = round(resultat, 0)
    if resultat - rounded_sum >= 0.44:
        resultat += 1
        print(f"The sum is {round(resultat, 0)}")
        return resultat
    else:
        print(f"The sum is {round(resultat, 0)}")
        return resultat


def tax_price(price):
    prices_list = price.split()
    the_sum = float(0)
    for i in prices_list:
        the_sum = the_sum + int(i)
    the_sum = the_sum * (1 - 6.5/100)
    return the_sum


def final_result():
    next_price = return_price()
    first_price = tax_price(next_price)
    is_discount = return_having()
    if is_discount == "yes":
        disc_type = discount_type()
        resultat = discount_amount(disc_type, first_price)
        rounding(resultat)
    else:
        print(first_price)


final_result()
