import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rotate(x, y, x0, y0, theta):
    """Поворот точек вокруг центра (x0, y0)"""
    x_rot = x - x0
    y_rot = y - y0
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    x_new = x_rot * cos_theta - y_rot * sin_theta + x0
    y_new = x_rot * sin_theta + y_rot * cos_theta + y0
    
    return x_new, y_new

def reuleaux_triangle(x, y, W, theta, N):
    """Создание треугольника Рёло"""
    # Углы для вершин равностороннего треугольника
    phi_vertices = [np.pi / 2 + 2 * np.pi / 3 * i for i in range(3)]
    
    # Радиус описанной окружности треугольника
    R = np.sqrt(3) * W / 3
    
    # Координаты вершин треугольника
    x0 = x + R * np.cos(phi_vertices)
    y0 = y + R * np.sin(phi_vertices)
    min_y = np.min(y0)
    
    # Создание первой дуги
    phi_arc = np.linspace(2 * np.pi / 3, np.pi - 0.001, N)
    x_1 = x + W / 2 + W * np.cos(phi_arc)
    y_1 = min_y + W * np.sin(phi_arc)
    
    # Создание второй и третьей дуг
    x_2, y_2 = rotate(x_1, y_1, x, y, 2 * np.pi / 3)
    x_3, y_3 = rotate(x_2, y_2, x, y, 2 * np.pi / 3)
    
    # Объединение точек контура
    x_out = np.concatenate([x_1, x_2, x_3, [x_1[0]]])
    y_out = np.concatenate([y_1, y_2, y_3, [y_1[0]]])
    
    # Вершины треугольника
    x_t = np.array([x_1[0], x_2[0], x_3[0]])
    y_t = np.array([y_1[0], y_2[0], y_3[0]])
    
    # Поворот всего контура на theta
    x_out, y_out = rotate(x_out, y_out, x, y, theta)
    x_t, y_t = rotate(x_t, y_t, x, y, theta)
    
    return x_out, y_out, x_t, y_t

# Параметры анимации
a = 1.0  # Длина стороны квадрата
N = 30   # Количество точек для построения треугольника Рёло
da = np.pi / 60  # Шаг угла

# Создание треугольника Рёло
x_out, y_out, x_t, y_t = reuleaux_triangle(0, 0, a, 0, N)
x_out, y_out = rotate(x_out, y_out, 0, 0, np.pi)
x_t, y_t = rotate(x_t, y_t, 0, 0, np.pi)

# Создание центрального круга
phi = np.arange(0, 2 * np.pi + np.pi / 20, np.pi / 20)
circ_radius = 0.15 / 7
x_circ = circ_radius * np.cos(phi)
y_circ = circ_radius * np.sin(phi)

# Вычисление параметров движения для всех четырёх сегментов
alpha = np.arange(0, np.pi / 6, da)
beta = np.pi / 3 - alpha
n = len(alpha)

# Матрица преобразования
H = np.array([[1, 1 / np.sqrt(3)],
              [1 / np.sqrt(3), 1]])

# Вычисление точек траектории для первого сегмента
cos_beta = np.cos(beta)
sin_beta = np.sin(beta)
A = a * np.vstack([2 - cos_beta - np.sqrt(3) * sin_beta,
                   2 - sin_beta - np.sqrt(3) * cos_beta]) / 2
B = a * np.vstack([np.ones(n),
                   1 - sin_beta])
C = a * np.vstack([1 - cos_beta,
                   np.ones(n)])
S = a - (a / 2) * H @ np.vstack([cos_beta, sin_beta])

# Расширение траектории на все четыре сегмента
S_full = np.hstack([
    S,
    rotate(S[0], S[1], a / 2, a / 2, -np.pi / 2),  # Второй сегмент
    rotate(S[0], S[1], a / 2, a / 2, -np.pi),      # Третий сегмент
    rotate(S[0], S[1], a / 2, a / 2, -3 * np.pi / 2)  # Четвёртый сегмент
])

# Настройка анимации
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# Отрисовка квадрата
square, = ax.plot([0, a, a, 0, 0], [0, 0, a, a, 0], 'b', lw=2)

# Отрисовка треугольника Рёло
triangle, = ax.plot([], [], 'b', lw=2)

# Отрисовка центрального стержня
rod = ax.fill([], [], 'k')[0]

# Добавим точку внутри треугольника
point, = ax.plot([], [], 'ro', markersize=5)  # Точка
trace, = ax.plot([], [], 'r-', lw=1)  # След точки

# Список для хранения координат следа
trace_x = []
trace_y = []

# Функция инициализации анимации
def init():
    triangle.set_data([], [])
    rod.set_xy(np.column_stack([[], []]))
    point.set_data([], [])
    trace.set_data([], [])
    return triangle, rod, point, trace

iter = 0
# Функция обновления кадра
def update(frame_idx):
    # Обновление позиции треугольника
    segment = frame_idx // n  # Определяем текущий сегмент
    angle_offset = -segment * np.pi / 2  # Угол смещения для текущего сегмента
    # print(angle_offset)
    x_rot, y_rot = rotate(x_out, y_out, 0, 0, -beta[frame_idx % n] + angle_offset)
    # print(x_rot[0], y_rot[0])
    # print(len(x_rot), len(y_rot))
    xp = x_rot + S_full[0, frame_idx]
    yp = y_rot + S_full[1, frame_idx]
    # print(xp[0], yp[0])
    triangle.set_data(xp, yp)


    # Обновление позиции центрального стержня
    xc = x_circ + S_full[0, frame_idx]
    yc = y_circ + S_full[1, frame_idx]
    rod.set_xy(np.column_stack([xc, yc]))

    global iter
    # Обновление позиции точки внутри треугольника
    # Фиксированная вершина (первая вершина)
    vertex_x = xp[0]
    vertex_y = yp[0]
    if iter < 30:
        if x_rot[0] < 0 and y_rot[0] < 0:
            vertex_x=xp[0]
            vertex_y = yp[0]
        if x_rot[0] < 0 and y_rot[0] > 0:
            vertex_x=xp[30]
            vertex_y = yp[30]
        if x_rot[0] > 0 and y_rot[0] > 0:
            vertex_x=xp[60]
            vertex_y = yp[60]
        if x_rot[0] > 0 and y_rot[0] < 0:
            vertex_x=xp[90]
            vertex_y = yp[90]
    if iter >= 30 and iter <= 60:
        if x_rot[0] < 0 and y_rot[0] < 0:
            vertex_x=xp[30]
            vertex_y = yp[30]
        if x_rot[0] < 0 and y_rot[0] > 0:
            vertex_x=xp[60]
            vertex_y = yp[60]
        if x_rot[0] > 0 and y_rot[0] > 0:
            vertex_x=xp[90]
            vertex_y = yp[90]
        if x_rot[0] > 0 and y_rot[0] < 0:
            vertex_x=xp[0]
            vertex_y = yp[0]
    if iter >= 60 and iter <= 90:
        if x_rot[0] < 0 and y_rot[0] < 0:
            vertex_x=xp[60]
            vertex_y = yp[60]
        if x_rot[0] < 0 and y_rot[0] > 0:
            vertex_x=xp[90]
            vertex_y = yp[90]
        if x_rot[0] > 0 and y_rot[0] > 0:
            vertex_x=xp[0]
            vertex_y = yp[0]
        if x_rot[0] > 0 and y_rot[0] < 0:
            vertex_x=xp[30]
            vertex_y = yp[30]
    if iter >= 90 and iter <= 120:
        if x_rot[0] < 0 and y_rot[0] < 0:
            vertex_x=xp[90]
            vertex_y = yp[90]
        if x_rot[0] < 0 and y_rot[0] > 0:
            vertex_x=xp[0]
            vertex_y = yp[0]
        if x_rot[0] > 0 and y_rot[0] > 0:
            vertex_x=xp[30]
            vertex_y = yp[30]
        if x_rot[0] > 0 and y_rot[0] < 0:
            vertex_x=xp[60]
            vertex_y = yp[60]
    iter +=1
    if iter >= 120:
        iter = 0

    # Центр треугольника
    center_x = np.mean(xp)
    center_y = np.mean(yp)
    # Сместим точку на 70% от центра к вершине
    t = 0.7  # Коэффициент смещения (0.5 — середина, 1 — вершина)
    x_point = center_x * (1 - t) + vertex_x * t
    y_point = center_y * (1 - t) + vertex_y * t
    point.set_data([x_point], [y_point])

    # Добавляем координаты точки в след
    trace_x.append(x_point)
    trace_y.append(y_point)
    trace.set_data(trace_x, trace_y)

    return triangle, rod, point, trace

# Создание анимации
ani = animation.FuncAnimation(
    fig, update, frames=range(S_full.shape[1]), init_func=init, blit=True, interval=50
)

# Показать анимацию
plt.show()