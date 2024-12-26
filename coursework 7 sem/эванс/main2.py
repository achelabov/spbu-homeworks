import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Задаем известные координаты точек A, D, F
A = np.array([0, 0])  # координаты точки A
D = np.array([4, 3])  # координаты точки D
F = np.array([6, 0])  # координаты точки F

# Задаем длины
Lab = 5
Lbc = 3
Lbe = 4
Lcd = 2
Lec = 3
Lef = 3

# Определяем функцию, которая будет представлять систему уравнений
def equations(vars):
    Xb, Yb, Xc, Yc, Xe, Ye = vars
    eq1 = (Xb - A[0])**2 + (Yb - A[1])**2 - Lab**2
    eq2 = (Xb - Xc)**2 + (Yb - Yc)**2 - Lbc**2
    eq3 = (Xb - Xe)**2 + (Yb - Ye)**2 - Lbe**2
    eq4 = (Xc - D[0])**2 + (Yc - D[1])**2 - Lcd**2
    eq5 = (Xe - Xc)**2 + (Ye - Yc)**2 - Lec**2
    eq6 = (Xe - F[0])**2 + (Ye - F[1])**2 - Lef**2
    return [eq1, eq2, eq3, eq4, eq5, eq6]

# Начальные предположения для решения
initial_guess = [1, 1, 2, 2, 5, 1]  # [Xb, Yb, Xc, Yc, Xe, Ye]

# Решаем систему уравнений
solution = fsolve(equations, initial_guess)

# Выводим решение
Xb, Yb, Xc, Yc, Xe, Ye = solution
print(f"Координаты точки B: ({Xb:.2f}, {Yb:.2f})")
print(f"Координаты точки C: ({Xc:.2f}, {Yc:.2f})")
print(f"Координаты точки E: ({Xe:.2f}, {Ye:.2f})")

# Визуализация
plt.figure(figsize=(8, 6))

# Рисуем известные точки
plt.plot(A[0], A[1], 'ro', label='A (0, 0)')
plt.plot(D[0], D[1], 'go', label='D (4, 3)')
plt.plot(F[0], F[1], 'bo', label='F (6, 0)')

# Рисуем найденные точки
plt.plot(Xb, Yb, 'ro', label='B')
plt.plot(Xc, Yc, 'go', label='C')
plt.plot(Xe, Ye, 'bo', label='E')

# Рисуем отрезки
plt.plot([A[0], Xb], [A[1], Yb], 'r--', label='AB')
plt.plot([Xb, Xc], [Yb, Yc], 'g--', label='BC')
plt.plot([Xb, Xe], [Yb, Ye], 'b--', label='BE')
plt.plot([Xc, D[0]], [Yc, D[1]], 'g--', label='CD')
plt.plot([Xe, Xc], [Ye, Yc], 'b--', label='EC')
plt.plot([Xe, F[0]], [Ye, F[1]], 'b--', label='EF')

# Настройки графика
plt.xlim(-1, 8)
plt.ylim(-1, 5)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Визуализация точек и отрезков')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

