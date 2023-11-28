# задача №1
# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого слова] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся константою
# або функцією input().

word = input("Enter the word: ")
length = len(word)

print(f"Word {word} has {length} letters")

# Задача №2
# Напишіть калькулятор, який запитує два числа якщо це множення, додавання, ділення, віднімання.
# Або одне число якщо це зняття коріння або піднесення до степіня.
# Виводить на екран результат.

c = 2  # будет вместо степеня, поскольку непонятно нужно ли спрашить у пользователя к какому степени подностиь
a = int(input("Enter the first number: "))
operation = input("Enter the operation: ")
if operation == "**" or operation == "1/2":
    if operation == "**":
        a = a**c
    else:
        a = a**(1/2)
    print(a)
else:
    b = int(input("Enter the second number: "))
    if operation == "+":
        a = a + b
    elif operation == "-":
        a = a - b
    elif operation == "*":
        a = a * b
    else:
        a = a // b
    print(a)





# Задача №3
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого повертає це число навпаки.
# Наприклад, користувач вводить 1234, а програма виводить 4321:
#
# Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число,
# яке складається з 4-х цифр, де кожна цифра може бути від 0 до 9 включно.
# Ваше рішення має це враховувати! Якщо користувач ввів щось не те повідомте йому.
#
number = input("Enter the number like this (1234): ")
num_list = list(number)
if number.isdigit():
    if len(number) > 4:
        print("Number is too big")
    else:
        dalatebale_item = num_list.pop(-1)
        new_list = dalatebale_item
        dalatebale_item = num_list.pop(-1)
        new_list = new_list + dalatebale_item
        dalatebale_item = num_list.pop(-1)
        new_list = new_list + dalatebale_item
        dalatebale_item = num_list.pop(-1)
        new_list = new_list + dalatebale_item
        print(new_list)
else:
    print("Wrong value")


print(f"{number[3]}{number[2]}{number[1]}{number[0]}")
