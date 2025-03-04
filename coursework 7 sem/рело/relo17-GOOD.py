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

def rolling_polygon(x, y, x1, y1, delta_a, figure_n):
    dx = np.diff(x)
    dy = np.diff(y)
    edge_lengths = np.sqrt(dx**2 + dy**2)
    edge_angles = np.arctan2(dy, dx)
    I = np.argmin(y)

    frames = []
    X = [x1.copy()]
    Y = [y1.copy()]

    for i in range(len(x) - 1):
        phi = edge_angles[I] if edge_angles[I] >= 0 else 2 * np.pi + edge_angles[I]

        if abs(edge_lengths[I]) < 1e-10:
            continue
        elif phi > delta_a:
            steps = int(np.ceil(phi / delta_a))
            phi2 = phi / steps
            for _ in range(steps):
                x, y = rotate(x, y, x[I], y[I], -phi2)
                x1, y1 = rotate(X[-1], Y[-1], x[I], y[I], -phi2)
                X.append(x1.copy())
                Y.append(y1.copy())
                frames.append((x.copy(), y.copy(), x1.copy(), y1.copy()))
        else:
            x, y = rotate(x, y, x[I], y[I], -phi)
            x1, y1 = rotate(X[-1], Y[-1], x[I], y[I], -phi)
            X.append(x1.copy())
            Y.append(y1.copy())
            frames.append((x.copy(), y.copy(), x1.copy(), y1.copy()))

        edge_angles -= edge_angles[I]
        I = (I + 1) % (len(x) - 1)

    return frames

# Пример использования
x = 0
y = 0
W = 1
theta = 0
N = 30
x_out, y_out, x_t, y_t = reuleaux_triangle(x, y, W, theta, N)

x1 = [0, x_t[0], 0]
y1 = [0, y_t[0], y_t[0] / 2]
frames = rolling_polygon(x_out, y_out, x1, y1, 2 * np.pi / (3 * 30), 1)

# Вычисление диапазонов осей
all_x = [frame[0] for frame in frames]
all_y = [frame[1] for frame in frames]
min_x = min([np.min(x) for x in all_x])
max_x = max([np.max(x) for x in all_x])
min_y = min([np.min(y) for y in all_y])
max_y = max([np.max(y) for y in all_y])

# Создание анимации
fig, ax = plt.subplots()
ax.set_xlim([min_x - 0.5, max_x + 0.5])
ax.set_ylim([min_y - 0.1, max_y + 0.1])
ax.set_aspect('equal')
ax.axis('off')

line, = ax.plot([], [], 'r')
point, = ax.plot([], [], 'go')

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(frame):
    x_frame, y_frame, x1_frame, y1_frame = frame
    line.set_data(x_frame, y_frame)
    point.set_data(x1_frame, y1_frame)
    return line, point

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.show()