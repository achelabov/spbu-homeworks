import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def reuleaux_triangle(x, y, W, theta, N):
    # Проверка входных данных
    if W <= 0:
        raise ValueError("W должно быть больше 0")
    if N <= 2:
        raise ValueError("N должно быть больше 2")

    # Вычисление углов вершин равностороннего треугольника
    phi = np.linspace(np.pi / 2, 2 * np.pi + np.pi / 2, 4)
    R = np.sqrt(3) * W / 3
    x0 = x + R * np.cos(phi)
    y0 = y + R * np.sin(phi)
    min_y = np.min(y0)

    # Создание одной дуги треугольника Рело
    phi = np.linspace(np.pi / 2 + np.pi / 6, np.pi - 0.001, N)
    x_1 = x + W / 2 + W * np.cos(phi)
    y_1 = min_y + W * np.sin(phi)

    # Создание других двух дуг путем вращения первой дуги вокруг центра треугольника
    x_2, y_2 = rotate(x_1, y_1, x, y, 2 * np.pi / 3)
    x_3, y_3 = rotate(x_2, y_2, x, y, 2 * np.pi / 3)

    # Объединение дуг
    x_out = np.concatenate((x_1, x_2, x_3, [x_1[0]]))
    y_out = np.concatenate((y_1, y_2, y_3, [y_1[0]]))

    # Пересчет вершин
    x_t = [x_1[0], x_2[0], x_3[0]]
    y_t = [y_1[0], y_2[0], y_3[0]]

    # Вращение на угол theta
    x_out, y_out = rotate(x_out, y_out, x, y, theta)
    x_t, y_t = rotate(x_t, y_t, x, y, theta)

    return x_out, y_out, x_t, y_t

def rotate(x, y, x_center, y_center, angle):
    # Вращение точек вокруг центра
    x = np.array(x)
    y = np.array(y)
    x_new = (x - x_center) * np.cos(angle) - (y - y_center) * np.sin(angle) + x_center
    y_new = (x - x_center) * np.sin(angle) + (y - y_center) * np.cos(angle) + y_center
    return x_new, y_new

def rolling_polygon(x, y, x1, y1, delta_a, prefix, figure_n):
    # Вычисление углов ребер
    dx = np.diff(x)
    dy = np.diff(y)
    edge_lengths = np.sqrt(dx**2 + dy**2)
    edge_angles = np.arctan2(dy, dx)
    I = np.argmin(y)

    # Создание фигуры для анимации
    fig, ax = plt.subplots(num=figure_n)
    ax.set_xlim([np.min(x) - 0.5, np.max(x) + 0.5 + np.sum(edge_lengths)])
    ax.set_ylim([-0.1, np.max(y) + 0.1])
    ax.set_aspect('equal')
    ax.axis('off')

    # Отслеживание точек
    X = [x1]
    Y = [y1]
    m = 1

    for i in range(len(x) - 1):
        if edge_angles[I] < 0:
            phi = 2 * np.pi + edge_angles[I]
        else:
            phi = edge_angles[I]

        # Если угол мал, выполняем один шаг, иначе делим на несколько шагов
        if abs(edge_lengths[I]) < 1e-10:
            continue
        elif phi > delta_a:
            steps = int(np.ceil(phi / delta_a))
            phi2 = phi / steps
            for j in range(steps):
                x, y = rotate(x, y, x[I], y[I], -phi2)
                x1, y1 = rotate(x1, y1, x[I], y[I], -phi2)
                X.append(x1)
                Y.append(y1)

                # Обновление фигуры
                ax.clear()
                ax.plot(x, y, 'r')
                ax.plot(X[-2:], Y[-2:], 'g')
                plt.savefig(f'{prefix}_{m:03d}.png')
                m += 1
        else:
            x, y = rotate(x, y, x[I], y[I], -phi)
            x1, y1 = rotate(x1, y1, x[I], y[I], -phi)
            X.append(x1)
            Y.append(y1)

            # Обновление фигуры
            ax.clear()
            ax.plot(x, y, 'r')
            ax.plot(X[-2:], Y[-2:], 'g')
            plt.savefig(f'{prefix}_{m:03d}.png')
            m += 1

        edge_angles = edge_angles - edge_angles[I]
        I = (I + 1) % (len(x) - 1)

    return X, Y

# Пример использования
x = 0
y = 0
W = 1
theta = 0
N = 30
x_out, y_out, x_t, y_t = reuleaux_triangle(x, y, W, theta, N)

x1 = [0, x_t[0], 0]
y1 = [0, y_t[0], y_t[0] / 2]
prefix = 'rolling_reuleux_tri'
rolling_polygon(x_out, y_out, x1, y1, 2 * np.pi / (3 * 30), prefix, 1)

# Создание анимации
fig, ax = plt.subplots()
ax.set_xlim([-1, 1 + np.pi])
ax.set_ylim([-0.1, np.max(y_out) + 0.1])
ax.set_aspect('equal')
ax.axis('off')

line, = ax.plot([], [], 'b')
point, = ax.plot([], [], 'go')

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(frame):
    line.set_data(x_out, y_out)
    point.set_data(x1, y1)
    return line, point

ani = FuncAnimation(fig, update, frames=range(360), init_func=init, blit=True)
plt.show()
