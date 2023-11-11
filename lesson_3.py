# Task_1
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось

product_list = input("Enter the list of products:")
product_list = product_list.replace(" ", "")
product_list = product_list.split(",")
elem_numb = len(product_list)

if elem_numb > 0:
    element_to_delete = int(input("Enter the number of product, you want to delete: ")) - 1
    product_list.pop(element_to_delete)
    elem_numb = elem_numb - 1
    print(product_list, "\n")

if elem_numb > 0:
    element_to_delete = int(input("Enter the number of product, you want to delete: ")) - 1
    product_list.pop(element_to_delete)
    elem_numb = elem_numb - 1
    print(product_list, "\n")

if elem_numb > 0:
    element_to_delete = int(input("Enter the number of product, you want to delete: ")) - 1
    product_list.pop(element_to_delete)
    elem_numb = elem_numb - 1
    print(product_list, "\n")

if elem_numb > 0:
    element_to_delete = int(input("Enter the number of product, you want to delete: ")) - 1
    product_list.pop(element_to_delete)
    elem_numb = elem_numb - 1
    print(product_list, "\n")

if elem_numb > 0:
    element_to_delete = int(input("Enter the number of product, you want to delete: ")) - 1
    product_list.pop(element_to_delete)
    elem_numb = elem_numb - 1
    print(product_list, "\n")

if elem_numb == 0:
    print("The list is empty\n")
else:
    print("The list is not empty\n")

new_product_list = input("Enter the list of products:")
new_product_list = new_product_list.replace(" ", "")
new_product_list = product_list + new_product_list.split(",")
print(f"Your list {new_product_list}")

# apple,juice,rice,tofu,chips,cola
