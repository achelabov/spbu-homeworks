import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import matplotlib.animation as animation

# Функция для ввода координат и длин
def input_variables():
    # Координаты известных точек
    Xa, Ya = -2, 5.5  # Координаты точки A
    Xc, Yc = -10, -10  # Координаты точки C

    # Длины стержней
    Loa = 5.5
    Lab = 10
    Lbc = 10
    Lbd = 10
    Lde = 15

    return (Xa, Ya), (Xc, Yc), Lab, Lbc, Lbd, Lde, Loa

# Определяем функцию, которая будет представлять систему уравнений
def equations(vars, A, C, lengths):
    Xb, Yb, Xd, Yd, Xe, Ye = vars
    Xa, Ya = A
    Xc, Yc = C
    Lab, Lbc, Lbd, Lde = lengths
    
    # Уравнения для определения координат точек B, D и E
    eq1 = (Xb - Xa)**2 + (Yb - Ya)**2 - Lab**2
    eq2 = (Xb - Xc)**2 + (Yb - Yc)**2 - Lbc**2
    eq3 = (Xb - Xd)**2 + (Yb - Yd)**2 - Lbd**2
    eq4 = (Xd - Xe)**2 + (Yd - Ye)**2 - Lde**2
    
    return [eq1, eq2, eq3, eq4]

# Функция для вычисления координат точки A
def calculate_A(t, Loa):
    phi = (np.pi / 50) * t  # Угловая скорость
    Xa = Loa * np.sin(phi)   # Координата X точки A
    Ya = Loa * np.cos(phi)   # Координата Y точки A
    return Xa, Ya

# Основная программа
def main():
    # Ввод известных переменных
    A, C, Lab, Lbc, Lbd, Lde, Loa = input_variables()
    
    # Начальные предположения для решения
    initial_guess = [-10.5, 0, -16, 10, -30, 8]  # [Xb, Yb, Xd, Yd, Xe, Ye]

    # Настройка анимации
    fig, ax = plt.subplots()
    ax.set_xlim(-40, 10)
    ax.set_ylim(-15, 15)

    # Линии для механизма
    line, = ax.plot([], [], 'ro-')  # Линия для механизма

    # Создаем текстовые метки для всех точек
    label_O = ax.text(0, 0, 'O', fontsize=12, ha='right', color='black')
    label_A = ax.text(0, 0, 'A', fontsize=12, ha='right', color='red')
    label_B = ax.text(0, 0, 'B', fontsize=12, ha='right', color='blue')
    label_C = ax.text(0, 0, 'C', fontsize=12, ha='right', color='purple')
    label_D = ax.text(0, 0, 'D', fontsize=12, ha='right', color='green')
    label_E = ax.text(0, 0, 'E', fontsize=12, ha='right', color='orange')

    # Массивы для хранения координат точки B
    Xb_history = []
    Yb_history = []

    # Текстовые метки для вывода координат, скорости и ускорения
    label_info = ax.text(-35, 10, '', fontsize=10, ha='left', color='black')

    def init():
        line.set_data([], [])
        return line, label_O, label_A, label_B, label_C, label_D, label_E, label_info

    def update(frame):
        # Вычисляем координаты точки A
        Xa, Ya = calculate_A(frame, Loa)
        A = (Xa, Ya)

        # Решаем систему уравнений для нахождения координат точек B, D и E
        solution = fsolve(equations, initial_guess, args=(A, C, (Lab, Lbc, Lbd, Lde)))
        Xb, Yb, Xd, Yd, Xe, Ye = solution

        # Сохраняем координаты точки B
        Xb_history.append(Xb)
        Yb_history.append(Yb)

        # Обновляем данные для анимации
        line.set_data([0, Xa, Xb, Xd, Xe], [0, Ya, Yb, Yd, Ye])

        # Обновляем текстовые метки для всех точек
        label_O.set_position((0, 0))
        label_A.set_position((Xa, Ya))
        label_B.set_position((Xb, Yb))
        label_C.set_position((C[0], C[1]))
        label_D.set_position((Xd, Yd))
        label_E.set_position((Xe, Ye))

        # Выводим координаты точки B в уголке графика
        label_info.set_text(f'B ({Xb:.2f}, {Yb:.2f})')

        # Соединяем точки O, A, B, C, D, E
        ax.plot([0, Xa], [0, Ya], 'r-')  # Линия OA
        ax.plot([Xa, Xb], [Ya, Yb], 'b-')  # Линия AB
        ax.plot([Xb, C[0]], [Yb, C[1]], 'b-')  # Линия BC
        ax.plot([Xb, Xd], [Yb, Yd], 'g-')  # Линия BD
        ax.plot([Xd, Xe], [Yd, Ye], 'orange')  # Линия DE

        return line, label_O, label_A, label_B, label_C, label_D, label_E, label_info

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200, 1), init_func=init, blit=True)
    plt.show()

if __name__ == "__main__":
    main()