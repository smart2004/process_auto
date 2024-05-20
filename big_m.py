import pulp
# Создание задачи линейного программирования
prob = pulp.LpProblem("Logical Constraints Example", pulp.LpMinimize)
# Создание переменных
x = pulp.LpVariable("x", 0, 1, pulp.LpBinary)
y = pulp.LpVariable("y", 0, 1, pulp.LpBinary)
# Добавление целевой функции
prob += x + y
# Добавление логических ограничений с использованием Big-M подхода
M = 1000
prob += x + M*y >= 1
# Решение задачи
prob.solve()
# Вывод результатов
print("Результат:")
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Значение целевой функции: ", pulp.value(prob.objective))
