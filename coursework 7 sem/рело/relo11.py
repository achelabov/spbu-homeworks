import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation

# Определяем точки
p1 = np.array([np.sqrt(3)/4, 0])
p2 = np.array([-np.sqrt(3)/4, -0.5])
p3 = np.array([-np.sqrt(3)/4, 0.5])

ps = [p1, p2, p3]

def rotate_point(point, angle):
    """Вращает точку на угол angle вокруг начала координат."""
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    rotation_matrix = np.array([[cos_theta, -sin_theta],
                                [sin_theta, cos_theta]])
    return np.dot(rotation_matrix, point)

def init():
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title('Theta: {:.2f}'.format(theta_values[0]))
    return []

def animate(i):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    theta = theta_values[i % len(theta_values)]
    ax.set_title('Theta: {:.2f}'.format(theta))
    
    # Вращаем точки треугольника
    rotated_ps = [rotate_point(p, theta) for p in ps]
    
    # Центральная точка (центр треугольника Рело)
    center = np.mean(rotated_ps, axis=0)
    ax.plot(center[0], center[1], 'ko')  # Черная точка в центре
    
    # Рисуем круги вокруг точек
    for p in rotated_ps:
        circle = Circle(p, 1, color=(0.5, 0.7, 0.8), alpha=0.33, ec='black', fill=True)
        ax.add_artist(circle)
    
    # Рисуем стороны треугольника Рело
    ax.plot([rotated_ps[0][0], rotated_ps[1][0]], [rotated_ps[0][1], rotated_ps[1][1]], 'k-', linewidth=1)
    ax.plot([rotated_ps[1][0], rotated_ps[2][0]], [rotated_ps[1][1], rotated_ps[2][1]], 'k-', linewidth=1)
    ax.plot([rotated_ps[2][0], rotated_ps[0][0]], [rotated_ps[2][1], rotated_ps[0][1]], 'k-', linewidth=1)
    
    # Линии и точки в зависимости от theta
    if -np.pi/6 <= theta < np.pi/6:
        point = rotated_ps[0]
        direction = np.array([1, 0])  # Параллельно оси X
        perpendicular = np.array([0, 1])
        
        ax.plot(point[0], point[1], 'ro', markersize=10)  # Красная точка на p1
        ax.plot([point[0] - 10*direction[0], point[0] + 10*direction[0]],
                [point[1] - 10*direction[1], point[1] + 10*direction[1]], 'b--', linewidth=0.5)  # Параллельная линия
        ax.plot([point[0] - 10*direction[0] - perpendicular[0], point[0] + 10*direction[0] - perpendicular[0]],
                [point[1] - 10*direction[1] - perpendicular[1], point[1] + 10*direction[1] - perpendicular[1]], 'b--', linewidth=0.5)  # Перпендикулярная линия
        ax.plot([point[0], point[0] - perpendicular[0]],
                [point[1], point[1] - perpendicular[1]], color=(0, 0.3, 0.4), linewidth=0.5)  # Линия к перпендикуляру
        
    elif np.pi/6 <= theta <= np.pi/2:
        point = rotated_ps[2]
        direction = np.array([1, 0])  # Параллельно оси X
        perpendicular = np.array([0, 1])
        
        ax.plot(point[0], point[1], 'ro', markersize=10)  # Красная точка на p3
        ax.plot([point[0] - 10*direction[0], point[0] + 10*direction[0]],
                [point[1] - 10*direction[1], point[1] + 10*direction[1]], 'b--', linewidth=0.5)  # Параллельная линия
        ax.plot([point[0] - 10*direction[0] - perpendicular[0], point[0] + 10*direction[0] - perpendicular[0]],
                [point[1] - 10*direction[1] - perpendicular[1], point[1] + 10*direction[1] - perpendicular[1]], 'b--', linewidth=0.5)  # Перпендикулярная линия
        ax.plot([point[0], point[0] - perpendicular[0]],
                [point[1], point[1] - perpendicular[1]], color=(0, 0.3, 0.4), linewidth=0.5)  # Линия к перпендикуляру
    
    return []

# Создаем значения theta
theta_values = np.concatenate((np.linspace(-np.pi/6, np.pi/2, 100), np.linspace(np.pi/2, -np.pi/6, 100)))

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=len(theta_values), init_func=init, blit=False, repeat=True)

# Отображаем анимацию
plt.show()