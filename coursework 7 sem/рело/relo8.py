import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры анимации
ROLLING_RADIUS = 1.0  # Радиус качения (равен ширине треугольника)
FLOOR_Y = -0.5        # Уровень поверхности качения

# Вершины исходного равностороннего треугольника
v1 = np.array([0.0, 0.0])
v2 = np.array([1.0, 0.0])
v3 = np.array([0.5, np.sqrt(3)/2])

# Вычисляем центроид и центрируем вершины
centroid = np.array([(v1[0]+v2[0]+v3[0])/3, (v1[1]+v2[1]+v3[1])/3])
v1_centered = v1 - centroid
v2_centered = v2 - centroid
v3_centered = v3 - centroid

# Функция генерации дуги
def generate_arc(center, start_point, end_point, num_points):
    vector_start = start_point - center
    vector_end = end_point - center
    theta_start = np.arctan2(vector_start[1], vector_start[0])
    theta_end = np.arctan2(vector_end[1], vector_end[0])
    if theta_end < theta_start:
        theta_end += 2 * np.pi
    theta = np.linspace(theta_start, theta_end, num_points)
    x = center[0] + np.cos(theta)
    y = center[1] + np.sin(theta)
    return x, y

# Генерируем дуги и центрируем
num_points = 100
x_arc1, y_arc1 = generate_arc(v3, v1, v2, num_points)
x_arc2, y_arc2 = generate_arc(v1, v2, v3, num_points)
x_arc3, y_arc3 = generate_arc(v2, v3, v1, num_points)

x = np.concatenate([x_arc1, x_arc2, x_arc3]) - centroid[0]
y = np.concatenate([y_arc1, y_arc2, y_arc3]) - centroid[1]

# Настройка анимации
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_aspect('equal')
ax.grid(True)
ax.set_ylim(FLOOR_Y - 0.5, FLOOR_Y + 1.5)

# Рисуем поверхность качения
floor_x = np.linspace(-5, 15, 2)
ax.plot(floor_x, [FLOOR_Y]*2, 'k-', lw=3, label='Поверхность качения')

# Элементы анимации
line, = ax.plot([], [], lw=2)
contact_point, = ax.plot([], [], 'go', markersize=8)  # Точка контакта
trajectory_line, = ax.plot([], [], 'r--', lw=1, alpha=0.7)  # Траектория центра
trace_line, = ax.plot([], [], 'b-', lw=1, alpha=0.5)   # След от треугольника
trajectory_data, trace_data = [], []

def init():
    line.set_data([], [])
    contact_point.set_data([], [])
    trajectory_line.set_data([], [])
    trace_line.set_data([], [])
    return line, contact_point, trajectory_line, trace_line

def update(frame):
    theta = frame * 2 * np.pi / 50  # Угол поворота
    x_translation = theta * ROLLING_RADIUS  # Смещение по X
    
    # Матрица вращения
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    # Вращаем и смещаем треугольник
    rotated_points = np.dot(rot_matrix, np.vstack([x, y]))
    rotated_points[0] += x_translation
    rotated_points[1] += FLOOR_Y + ROLLING_RADIUS  # Опускаем на уровень поверхности
    
    # Точка контакта с поверхностью
    contact_x = x_translation
    contact_y = FLOOR_Y
    
    # Обновляем данные
    line.set_data(rotated_points[0], rotated_points[1])
    contact_point.set_data([contact_x], [contact_y])
    
    # Траектория центра качения
    trajectory_data.append((x_translation, FLOOR_Y + ROLLING_RADIUS))
    trajectory_line.set_data(*zip(*trajectory_data))
    
    # След от треугольника
    trace_data.extend(zip(rotated_points[0], rotated_points[1]))
    if len(trace_data) > 500:
        trace_data.pop(0)
    trace_line.set_data(*zip(*trace_data))
    
    # Динамическое смещение области просмотра
    ax.set_xlim(contact_x - 3, contact_x + 5)
    
    return line, contact_point, trajectory_line, trace_line

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=20)
plt.legend()
plt.title("Качение треугольника Рело с визуализацией поверхности и траекторий")
plt.show()