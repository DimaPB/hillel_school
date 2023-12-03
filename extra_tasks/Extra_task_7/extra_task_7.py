# Задача №7
# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0.
# Для порожнього масиву результат завжди 0.
# Пояснення:
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

unresolved_list = [1, 3, 5]


def solved_list(unsorted_list: list):
    sorted_list = []
    for i in unsorted_list[::2]:
        sorted_list.append(i)
    return sorted_list


if not unresolved_list:
    result = 0
    print(result)
else:
    last_elem = unresolved_list[-1]
    print(last_elem)

    solved_list = sum(solved_list(unresolved_list))
    print(solved_list)

    result = solved_list * last_elem
    print(result)





