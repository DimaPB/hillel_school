# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
#
# __ne__: To check if two objects are not equal.
#
# __lt__: To check if one object is less than another.
#
# __le__: To check if one object is less than or equal to another.
#
# __gt__: To check if one object is greater than another.
#
# __ge__: To check if one object is greater than or equal to another.
#
# Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода
# __eq__ який ми розглянули на уроці. Тобто вам треба буде змінити всього дві букви.
#
# І написати свою логіку яку ви хочте.
#
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює

# class Chort:
#     def __init__(self, name):
#         if name == "Volodia":
#             print(f"{name} в натуре чорт")
#         else:
#             print(f"{name} мій пацан")
#
#
# Name = Chort("Dimon")

class TheSquare:

    def __init__(self, number, number_rate):
        self.number = number
        self.number_rate = number_rate

    def __gt__(self, other):
        result = self.number ** self.number_rate
        print(result)
        return result


number_one = TheSquare(3, 3)
number_two = TheSquare(3, 3)

print(number_one != number_two)
