# Задача №3
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого повертає це число навпаки.
# Наприклад, користувач вводить 1234, а програма виводить 4321:
#
# Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число,
# яке складається з 4-х цифр, де кожна цифра може бути від 0 до 9 включно.
# Ваше рішення має це враховувати! Якщо користувач ввів щось не те повідомте йому.
#
number = input("Enter the number: ")
num_list = list(number)

dalatebale_item = num_list.pop(-1)
new_list = dalatebale_item
dalatebale_item = num_list.pop(-1)
new_list = new_list + dalatebale_item
dalatebale_item = num_list.pop(-1)
new_list = new_list + dalatebale_item
dalatebale_item = num_list.pop(-1)
new_list = new_list + dalatebale_item
print(new_list)

