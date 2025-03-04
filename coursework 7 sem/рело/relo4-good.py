import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Вершины исходного равностороннего треугольника
v1 = np.array([0.0, 0.0])
v2 = np.array([1.0, 0.0])
v3 = np.array([0.5, np.sqrt(3)/2])

# Вычисляем центроид
centroid = np.array([(v1[0] + v2[0] + v3[0])/3, (v1[1] + v2[1] + v3[1])/3])

# Функция генерации дуги
def generate_arc(center, start_point, end_point, num_points):
    vector_start = start_point - center
    vector_end = end_point - center
    theta_start = np.arctan2(vector_start[1], vector_start[0])
    theta_end = np.arctan2(vector_end[1], vector_end[0])
    if theta_end < theta_start:
        theta_end += 2 * np.pi
    theta = np.linspace(theta_start, theta_end, num_points)
    x = center[0] + np.cos(theta)  # радиус = 1.0
    y = center[1] + np.sin(theta)
    return x, y

# Генерируем дуги с центрами в исходных вершинах
num_points = 100
x_arc1, y_arc1 = generate_arc(v3, v1, v2, num_points)
x_arc2, y_arc2 = generate_arc(v1, v2, v3, num_points)
x_arc3, y_arc3 = generate_arc(v2, v3, v1, num_points)

# Объединяем и центрируем все точки
x = np.concatenate([x_arc1, x_arc2, x_arc3])
y = np.concatenate([y_arc1, y_arc2, y_arc3])
x_centered = x - centroid[0]
y_centered = y - centroid[1]

# Настраиваем анимацию и квадрат
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(-0.7, 0.7)

# Рисуем квадрат 1x1
square_side = 1.15
square_x = [-square_side/2, square_side/2, square_side/2, -square_side/2, -square_side/2]
square_y = [-square_side/2, -square_side/2, square_side/2, square_side/2, -square_side/2]
ax.plot(square_x, square_y, 'r--', label='Квадрат 1.15x1.15') # TODO: Почему именно такой размер квадрата? Необходимо в будущем обхяснить

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    theta = frame * 2 * np.pi / 100
    rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta),  np.cos(theta)]])
    rotated_points = np.dot(rot_matrix, np.vstack([x_centered, y_centered]))
    line.set_data(rotated_points[0], rotated_points[1])
    return line,

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=20)
plt.legend()
plt.show()