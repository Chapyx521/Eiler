import math

# Функция f(x, y)
def f(x, y):
    return (2 * y**2 * math.log(x) - y) / x
# Начальные условия
x0 = 0.5
y0 = 0.897
h = 0.2
# Диапазон значений x
x_values = [x0 + i * h for i in range(21)]
# Списки для хранения значений y, f(x, y) и ошибки
y_values = [y0]
f_values = [f(x0, y0)]
error_values = []
# Метод Эйлера
for i in range(len(x_values) - 1):
    y_next = y_values[-1] + h * f(x_values[i], y_values[i])
    y_values.append(y_next)
    f_values.append(f(x_values[i + 1], y_next))
# Вывод таблицы
print("| Iteration | x_k        | f(x_k, y_k)  | y_k        |")
print("|-----------|------------|--------------|------------|")
for i in range(len(x_values)):
    print(f"| {i:^9} | {x_values[i]:11.8f} | {f_values[i]:12.8f} | {y_values[i]:11.8f} |")
