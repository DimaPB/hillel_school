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

class TheDegree:

    def __init__(self, number, degree):
        self.number = number
        self.degree = degree

    def __gt__(self, other):
        print(self.number ** self.degree, other.number ** other.degree)
        return self.number ** self.degree > other.number ** other.degree


number_one = TheDegree(2, 11)
number_two = TheDegree(3, 7)
print(number_one > number_two)