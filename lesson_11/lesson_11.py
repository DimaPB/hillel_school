# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента,
# та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати
# імя студента. другий метод буде виводити оцінки. Методи виводять результат через прінти.
#
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі).
# Вивідіть дві функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.
#
# 3) обновіть requirements.txt
#
# ВСІ ЗАВДАННЯ ПОВИННІ БУТИ ПЕРЕВІРЕННІ flake8 за кожну помилку яку він знайде
# (окрім E501(там де кількість стрічок в ряд))буду знімати по 10 балів.


class Student:
    name = "Arthur"
    marks = [1, 2, 3, 4]

    def say_hello(self):
        self.print_name = f"Hi, my name is {self.name}"
        print(self.print_name)

    def my_marks(self):
        self.print_marks = f"That`s my marks: {self.marks}"
        print(self.print_marks)


student = Student()
new_student = Student()
new_student.name = "Dmytro"
student.say_hello()
student.my_marks()
new_student.say_hello()
new_student.my_marks()

