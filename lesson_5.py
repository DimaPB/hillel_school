# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно)
# (так як робили на уроці).
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.

table = {"+": [], "-": [], "*": [], "/": []}
for i in range(2, 10):
    for j in range(2, 10):
        table["+"].append(f"{i}+{j}={i+j}")
        table["-"].append(f"{i}-{j}={i-j}")
        table["*"].append(f"{i}*{j}={i*j}")
        table["/"].append(f"{i}/{j}={round(i/j, 2)}")
operation = input("Select the operation: ")
print(table[operation])
