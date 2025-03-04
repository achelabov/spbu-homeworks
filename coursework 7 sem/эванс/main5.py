import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import matplotlib.animation as animation

# Функция для ввода координат и длин
def input_variables():
    # Координаты известных точек
    Xa, Ya = 2.5, 1.5  # Координаты точки A
    Xd, Yd = 6, 9      # Координаты точки D
    Xf, Yf = -4.3, 20  # Координаты точки F

    # Длины стержней
    Lab = 11
    Lbc = 4
    Lbe = 9
    Lcd = 5.5
    Lec = 5
    Lef = 10
    Loa = 3  # Длина OA

    return (Xa, Ya), (Xd, Yd), (Xf, Yf), Lab, Lbc, Lbe, Lcd, Lec, Lef, Loa

# Определяем функцию, которая будет представлять систему уравнений
def equations(vars, A, D, F, lengths):
    Xb, Yb, Xc, Yc, Xe, Ye = vars
    Xa, Ya = A
    Xd, Yd = D
    Xf, Yf = F
    Lab, Lbc, Lbe, Lcd, Lec, Lef = lengths
    
    # Уравнения для определения координат точек B, C и E
    eq1 = (Xb - Xa)**2 + (Yb - Ya)**2 - Lab**2
    eq2 = (Xb - Xc)**2 + (Yb - Yc)**2 - Lbc**2
    eq3 = (Xb - Xe)**2 + (Yb - Ye)**2 - Lbe**2
    eq4 = (Xc - Xd)**2 + (Yc - Yd)**2 - Lcd**2
    eq5 = (Xe - Xc)**2 + (Ye - Yc)**2 - Lec**2
    eq6 = (Xe - Xf)**2 + (Ye - Yf)**2 - Lef**2
    
    return [eq1, eq2, eq3, eq4, eq5, eq6]

# Функция для вычисления координат точки A
def calculate_A(t, Loa):
    phi = (np.pi / 50) * t  # Угловая скорость
    Xa = Loa * np.sin(phi)   # Координата X точки A
    Ya = Loa * np.cos(phi)   # Координата Y точки A
    return Xa, Ya

# Основная программа
def main():
    # Ввод известных переменных
    A, D, F, Lab, Lbc, Lbe, Lcd, Lec, Lef, Loa = input_variables()
    
    # Начальные предположения для решения
    initial_guess = [4.3, 11, 0.2, 10, -4.5, 9]  # [Xb, Yb, Xc, Yc, Xe, Ye]

    # Настройка анимации
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-5, 25)

    # Линии для механизма
    line, = ax.plot([], [], 'ro-')  # Линия для механизма
    line2, = ax.plot([], [], 'ro-') # CD
    line3, = ax.plot([], [], 'ro-') # FE

    # Создаем текстовые метки для всех точек
    label_O = ax.text(0, 0, 'O', fontsize=12, ha='right', color='black')
    label_A = ax.text(0, 0, 'A', fontsize=12, ha='right', color='red')
    label_B = ax.text(0, 0, 'B', fontsize=12, ha='right', color='blue')
    label_C = ax.text(0, 0, 'C', fontsize=12, ha='right', color='purple')
    label_E = ax.text(0, 0, 'E', fontsize=12, ha='right', color='orange')
    label_D = ax.text(0, 0, 'D', fontsize=12, ha='right', color='green')
    label_F = ax.text(0, 0, 'F', fontsize=12, ha='right', color='blue')

    # Массивы для хранения координат точки B
    Xb_history = []
    Yb_history = []

    # Текстовые метки для вывода координат, скорости и ускорения
    label_info = ax.text(-14, 20, '', fontsize=10, ha='left', color='black')

    def init():
        line.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        return line, line2, line3, label_O, label_A, label_B, label_C, label_E, label_D, label_F, label_info

    def update(frame):
        # Вычисляем координаты точки A
        Xa, Ya = calculate_A(frame, Loa)
        A = (Xa, Ya)

        # Решаем систему уравнений для нахождения координат точек B, C и E
        solution = fsolve(equations, initial_guess, args=(A, D, F, (Lab, Lbc, Lbe, Lcd, Lec, Lef)))
        Xb, Yb, Xc, Yc, Xe, Ye = solution

        # Сохраняем координаты точки B
        Xb_history.append(Xb)
        Yb_history.append(Yb)

        # Вычисляем скорость точки B с помощью конечных разностей
        if len(Xb_history) > 1:
            VxB = (Xb_history[-1] - Xb_history[-2]) / 1  # Делим на 1, так как шаг времени равен 1
            VyB = (Yb_history[-1] - Yb_history[-2]) / 1
        else:
            VxB, VyB = 0, 0  # Начальная скорость

        # Вычисляем ускорение точки B
        if len(Xb_history) > 2:
            AxB = (Xb_history[-1] - 2 * Xb_history[-2] + Xb_history[-3]) / (1**2)  # Второй порядок
            AyB = (Yb_history[-1] - 2 * Yb_history[-2] + Yb_history[-3]) / (1**2)
        else:
            AxB, AyB = 0, 0  # Начальное ускорение

        # Обновляем данные для анимации
        line.set_data([0, Xa, Xb, Xc, Xe], [0, Ya, Yb, Yc, Ye])
        line2.set_data([Xc, D[0]], [Yc, D[1]])
        line3.set_data([Xe, F[0]], [Ye, F[1]])

        # Обновляем текстовые метки для всех точек
        label_O.set_position((0, 0))
        label_A.set_position((Xa, Ya))
        label_B.set_position((Xb, Yb))
        label_C.set_position((Xc, Yc))
        label_E.set_position((Xe, Ye))
        label_D.set_position((D[0], D[1]))
        label_F.set_position((F[0], F[1]))

        # Выводим координаты, скорость и ускорение в уголке графика
        label_info.set_text(f'B ({Xb:.2f}, {Yb:.2f})\nVb ({VxB:.2f}, {VyB:.2f})\nAb ({AxB:.2f}, {AyB:.2f})')

        # Соединяем точки O, A, B, C, D, E, F
        ax.plot([0, Xa], [0, Ya], 'r-')  # Линия OA
        ax.plot([Xa, Xb], [Ya, Yb], 'b-')  # Линия AB
        ax.plot([Xb, Xc], [Yb, Yc], 'b-')  # Линия BC
        ax.plot([Xc, D[0]], [Yc, D[1]], 'g-')  # Линия CD
        ax.plot([Xe, F[0]], [Ye, F[1]], 'b-')  # Линия EF
        ax.plot([Xc, Xe], [Yc, Ye], 'orange')  # Линия CE

        return line, line2, line3, label_O, label_A, label_B, label_C, label_E, label_D, label_F, label_info

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200, 1), init_func=init, blit=True)
    plt.show()
 
    # Построение зависимостии Xb от Yb
    plt.figure()
    plt.plot(Xb_history, Yb_history, 'b-')
    plt.xlabel('Xb')
    plt.ylabel('Yb')
    plt.title('Построение зависимостии Xb от Yb')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()