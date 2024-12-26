import numpy as np
from scipy.optimize import fsolve

# Функция для ввода координат и длин
def input_variables():
    # Координаты известных точек
    Xa, Ya = 2.5, 1.5
    Xd, Yd = 6, 9
    Xf, Yf = -4.3, 20

    # Длины стержней
    Lab = 11
    Lbc = 4
    Lbe = 9
    Lcd = 5.5
    Lec = 5
    Lef = 10

    
    return (Xa, Ya), (Xd, Yd), (Xf, Yf), Lab, Lbc, Lbe, Lcd, Lec, Lef

# Определяем функцию, которая будет представлять систему уравнений
def equations(vars, A, D, F, lengths):
    Xb, Yb, Xc, Yc, Xe, Ye = vars
    Xa, Ya = A
    Xd, Yd = D
    Xf, Yf = F
    Lab, Lbc, Lbe, Lcd, Lec, Lef = lengths
    
    eq1 = (Xb - Xa)**2 + (Yb - Ya)**2 - Lab**2
    eq2 = (Xb - Xc)**2 + (Yb - Yc)**2 - Lbc**2
    eq3 = (Xb - Xe)**2 + (Yb - Ye)**2 - Lbe**2
    eq4 = (Xc - Xd)**2 + (Yc - Yd)**2 - Lcd**2
    eq5 = (Xe - Xc)**2 + (Ye - Yc)**2 - Lec**2
    eq6 = (Xe - Xf)**2 + (Ye - Yf)**2 - Lef**2
    
    return [eq1, eq2, eq3, eq4, eq5, eq6]

# Основная программа
def main()
    # Ввод известных переменных
    A, D, F, Lab, Lbc, Lbe, Lcd, Lec, Lef = input_variables()
    
    # Начальные предположения для решения
    initial_guess = [4.3, 11, 0.2, 10, -4.5, 9]  # [Xb, Yb, Xc, Yc, Xe, Ye]

    # Решаем систему уравнений
    solution = fsolve(equations, initial_guess, args=(A, D, F, (Lab, Lbc, Lbe, Lcd, Lec, Lef)))

    # Выводим решение
    Xb, Yb, Xc, Yc, Xe, Ye = solution
    print(f"Координаты точки B: ({Xb:.2f}, {Yb:.2f})")
    print(f"Координаты точки C: ({Xc:.2f}, {Yc:.2f})")
    print(f"Координаты точки E: ({Xe:.2f}, {Ye:.2f})")

if __name__ == "__main__":
    main()

