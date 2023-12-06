# 1) додайте requirements.txt на ваш гіт
# 2) Виберіть будь-яку помилку яка вам подобається
# і зробіть функцію яка перевіряє на цю помилку(в функції try except)
# 3) зробіть функцію як ми робили з додаванням
# тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

from datetime import datetime


def time_counter(func):
    def counter(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        print(delta_time)
        return result
    return counter


@time_counter
def list_check(the_list):
    list_sum = 0
    try:
        for i in the_list:
            list_sum = list_sum + i
        print(list_sum)
    except(TypeError):
        print("There is an unexpected type in the list")

    return list_sum


list_params = [1, 2, 3,]  # [1, 2, "3"]
list_check(list_params)


def add_tree_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


# add_two_numbers(1, 2,3)




