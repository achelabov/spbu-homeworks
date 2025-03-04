import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def reuleaux_triangle(x, y, W, theta, N):
    if W <= 0:
        raise ValueError("W должно быть больше 0")
    if N <= 2:
        raise ValueError("N должно быть больше 2")

    phi = np.linspace(np.pi / 2, 2 * np.pi + np.pi / 2, 4)
    R = np.sqrt(3) * W / 3
    x0 = x + R * np.cos(phi)
    y0 = y + R * np.sin(phi)
    min_y = np.min(y0)

    phi = np.linspace(np.pi / 2 + np.pi / 6, np.pi - 0.001, N)
    x_1 = x + W / 2 + W * np.cos(phi)
    y_1 = min_y + W * np.sin(phi)

    x_2, y_2 = rotate(x_1, y_1, x, y, 2 * np.pi / 3)
    x_3, y_3 = rotate(x_2, y_2, x, y, 2 * np.pi / 3)

    x_out = np.concatenate((x_1, x_2, x_3, [x_1[0]]))
    y_out = np.concatenate((y_1, y_2, y_3, [y_1[0]]))

    x_t = [x_1[0], x_2[0], x_3[0]]
    y_t = [y_1[0], y_2[0], y_3[0]]

    x_out, y_out = rotate(x_out, y_out, x, y, theta)
    x_t, y_t = rotate(x_t, y_t, x, y, theta)

    return x_out, y_out, x_t, y_t

def rotate(x, y, x_center, y_center, angle):
    x = np.array(x)
    y = np.array(y)
    x_new = (x - x_center) * np.cos(angle) - (y - y_center) * np.sin(angle) + x_center
    y_new = (x - x_center) * np.sin(angle) + (y - y_center) * np.cos(angle) + y_center
    return x_new, y_new

# Параметры квадрата
a = 1
square_x = [0, a, a, 0, 0]
square_y = [0, 0, a, a, 0]

# Параметры треугольника Рело
W = 1
N = 30
theta = 0

# Центр масс треугольника
def center_of_mass(beta):
    H = np.array([[1, 1 / np.sqrt(3)], [1 / np.sqrt(3), 1]])
    vec = np.array([np.cos(beta), np.sin(beta)])
    S = a - (a / 2) * H @ vec
    return S

# Генерация траектории центра масс
da = np.pi / 60
alpha = np.arange(0, np.pi / 6, da)
beta = np.pi / 3 - alpha
S = np.array([center_of_mass(b) for b in beta]).T

# Полный оборот
S_full = np.hstack([
    S,
    np.array([rotate(S[0], S[1], a / 2, a / 2, -np.pi / 2)]).reshape(2, -1),
    np.array([rotate(S[0], S[1], a / 2, a / 2, -np.pi)]).reshape(2, -1),
    np.array([rotate(S[0], S[1], a / 2, a / 2, -3 * np.pi / 2)]).reshape(2, -1),
    np.array([rotate(S[0], S[1], a / 2, a / 2, -2 * np.pi)]).reshape(2, -1)
])

# Создание анимации
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.axis('off')

# Отрисовка квадрата
ax.plot(square_x, square_y, 'b-', linewidth=2)

# Отрисовка треугольника
triangle, = ax.plot([], [], 'r-', linewidth=2)
center, = ax.plot([], [], 'ro')

def init():
    triangle.set_data([], [])
    center.set_data([], [])
    return triangle, center

def update(frame):
    # Угол поворота
    angle = frame * da

    # Вращение треугольника
    x_out, y_out, x_t, y_t = reuleaux_triangle(0, 0, W, angle, N)
    x_out, y_out = rotate(x_out, y_out, 0, 0, -np.pi / 3)
    x_t, y_t = rotate(x_t, y_t, 0, 0, -np.pi / 3)

    # Перемещение треугольника
    x_out += S_full[0, frame % S_full.shape[1]]
    y_out += S_full[1, frame % S_full.shape[1]]
    x_t += S_full[0, frame % S_full.shape[1]]
    y_t += S_full[1, frame % S_full.shape[1]]

    # Отрисовка
    triangle.set_data(x_out, y_out)
    center.set_data([S_full[0, frame % S_full.shape[1]]], [S_full[1, frame % S_full.shape[1]]])  # Исправлено

    return triangle, center

# Запуск анимации
ani = FuncAnimation(fig, update, frames=range(S_full.shape[1] * 4), init_func=init, blit=True, interval=50)
plt.show()