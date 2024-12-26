import numpy as np
from scipy.optimize import fsolve

# Длины
Loa = 5.5
Lab = 10
Lbc = 10
Lbd = 10
Lde = 15

# Известные координаты
Xa, Ya = -2, 5.5
Xc, Yc = -10, -10
Ye = 8

# Функция, представляющая систему уравнений
def equations(vars):
    Xb, Xd, Xe = vars
    Yb = (Lab**2 - (Xb - Xa)**2)**0.5 + Ya  # Выражаем Yb через Xb
    Yd = (Lbd**2 - (Xb - Xd)**2)**0.5 + Yb  # Выражаем Yd через Xb и Xd
    return [
        (Xb - Xc)**2 + (Yb - Yc)**2 - Lbc**2,  # Уравнение для B и C
        (Xd - Xb)**2 + (Yd - Yb)**2 - Lbd**2,  # Уравнение для B и D
        (Xd - Xe)**2 + (Yd - Ye)**2 - Lde**2   # Уравнение для D и E
    ]

# Начальные предположения для Xb, Xd и Xe
initial_guess = [0, 0, 0]

# Решение системы уравнений
solution = fsolve(equations, initial_guess)

# Xb, Xd, Xe = solution
# Yb = (Lab**2 - (Xb - Xa)**2)**0.5 + Ya
# Yd = (Lbd**2 - (Xb - Xd)**2)**0.5 + Yb

def GetSolution():
    Xb, Xd, Xe = solution
    Yb = (Lab**2 - (Xb - Xa)**2)**0.5 + Ya
    Yd = (Lbd**2 - (Xb - Xd)**2)**0.5 + Yb
    return Xb, Xd, Xe, Yb, Yd

# print(f"Координаты точки B: ({Xb}, {Yb})")
# print(f"Координаты точки D: ({Xd}, {Yd})")
# print(f"Координаты точки E: ({Xe}, {Ye})")
