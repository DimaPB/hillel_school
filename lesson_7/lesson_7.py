#1) сортування списка по зростанню числа, від меншого до більшого.
# Функція приймає список з чисел і повертає відсортований список.


def sorted_list(new_list: list) -> list:
    new_list = sorted(new_list)
    return new_list


list_1 = sorted_list([2, 1, 4, 5, -1, 3])
print(list_1)


# 2) сортування списка на спад, від  більшого до меншого.
# Функція приймає список з чисел і повертає відсортований список.


def reversed_list(new_list: list) -> list:
    new_list = sorted(new_list, reverse=True)
    return new_list


list_2 = reversed_list([2, 1, 4, 5, 3])
print(list_2)


# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
# apple,juice,rice,tofu,chips,cola,ice


def words_list(words: list) -> list:
    words = sorted(words, key=len)
    return words


list_3 = words_list(["apple", "juice", "rice", "tofu", "chips", "cola", "ice"])
print(list_3)
