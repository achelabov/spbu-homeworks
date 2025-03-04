import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Параметры треугольника Рело
radius = 1.0  # радиус окружностей
num_points = 500  # количество точек для построения
width = radius  # постоянная ширина

# Создаём точки для треугольника Рело
def create_reuleaux_points():
    angles = np.linspace(0, 2*np.pi, num_points)
    
    # Вершины равностороннего треугольника
    vertices = np.array([
        [0.0, 0.0],
        [radius, 0.0],
        [radius/2, (np.sqrt(3)/2)*radius]
    ])
    
    # Генерация трёх дуг
    points = []
    for i in range(3):
        center = vertices[i]
        start_angle = (2*np.pi/3)*i - np.pi/6
        end_angle = start_angle + 2*np.pi/3
        theta = np.linspace(start_angle, end_angle, num_points//3)
        x = center[0] + radius * np.cos(theta)
        y = center[1] + radius * np.sin(theta)
        points.extend(list(zip(x, y)))
    
    return np.array(points)

# Инициализация фигуры
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-1, 3)
ax.set_ylim(-0.5, 1.5)

# Горизонтальные линии
line_top = ax.axhline(y=width, color='g', linestyle='-', lw=2)
line_bottom = ax.axhline(y=0, color='g', linestyle='-', lw=2)

# Объекты для анимации
reuleaux_line, = ax.plot([], [], 'r-', lw=2)
trace_line, = ax.plot([], [], 'b--', lw=1)
width_text = ax.text(0.05, 0.95, f'Constant Width: {width}', 
                    transform=ax.transAxes, fontsize=12)

# Предварительный расчёт точек
points = create_reuleaux_points()
x_center = 0.0  # начальная позиция центра

# Функция анимации
def animate(frame):
    global x_center
    
    # Параметры движения
    angle = np.radians(frame)
    x_center += 0.05  # смещение центра
    
    # Поворот и смещение точек
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Центрирование и поворот
    rotated_points = (points - [radius/2, (np.sqrt(3)/6)*radius]).dot(rotation_matrix) + [x_center, width/2]
    
    # Обновление графики
    reuleaux_line.set_data(rotated_points[:,0], rotated_points[:,1])
    
    # Обновление следа центра
    old_data = trace_line.get_data()
    trace_line.set_data(
        np.append(old_data[0], x_center),
        np.append(old_data[1], width/2)
    )
    
    # Проверка выхода за границы
    if x_center > 2.5:
        x_center = -0.5
        trace_line.set_data([], [])
    
    return reuleaux_line, trace_line

# Создание анимации
ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    frames=np.arange(0, 360, 2),
    interval=50,
    blit=True
)

plt.show()