import matplotlib.pyplot as plt

# Данные для первого графика
elements1 = [10, 50, 100, 500, 1000]
time1 = [0.01, 0.05, 0.1, 0.5, 1.0]

# Данные для второго графика
elements2 = [10, 50, 100, 500, 1000]
time2 = [0.02, 0.07, 0.15, 0.6, 1.2]

# Данные для третьего графика
elements3 = [10, 50, 100, 500, 1000]
time3 = [0.03, 0.08, 0.2, 0.7, 1.4]

# Первый график
plt.figure()
plt.plot(elements1, time1, marker='o')
plt.title('Зависимость времени от количества элементов (График 1)')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.grid(True)

# Второй график
plt.figure()
plt.plot(elements2, time2, marker='o')
plt.title('Зависимость времени от количества элементов (График 2)')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.grid(True)

# Третий график
plt.figure()
plt.plot(elements3, time3, marker='o')
plt.title('Зависимость времени от количества элементов (График 3)')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.grid(True)

# Отобразить все графики
plt.show()
