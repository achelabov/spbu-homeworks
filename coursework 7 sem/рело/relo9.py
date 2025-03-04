import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Определяем точки
p1 = np.array([np.sqrt(3)/4, 0])
p2 = np.array([-np.sqrt(3)/4, -0.5])
p3 = np.array([-np.sqrt(3)/4, 0.5])

ps = [p1, p2, p3]

def min_theta(theta):
    if -np.pi/3 < theta < np.pi/3:
        return np.linalg.norm(ps[0])
    else:
        return 0

def graphics(theta):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    # Рисуем круги вокруг точек
    for p in ps:
        circle = Circle(p, 1, color=(0.5, 0.7, 0.8), alpha=0.33, ec='black', fill=True)
        ax.add_artist(circle)
    
    # Центральная точка
    center = np.mean(ps, axis=0)
    ax.plot(center[0], center[1], 'ko')
    
    # Линии и точки в зависимости от theta
    if -np.pi/6 <= theta < np.pi/6:
        point = p1
        direction = np.array([np.sin(theta), np.cos(theta)])
        perpendicular = np.array([np.cos(theta), -np.sin(theta)])
        
        ax.plot(point[0], point[1], 'ro', markersize=10)
        ax.plot([point[0] - 10*direction[0], point[0] + 10*direction[0]],
                [point[1] - 10*direction[1], point[1] + 10*direction[1]], 'b-', linewidth=0.5)
        ax.plot([point[0] - 10*direction[0] - perpendicular[0], point[0] + 10*direction[0] - perpendicular[0]],
                [point[1] - 10*direction[1] - perpendicular[1], point[1] + 10*direction[1] - perpendicular[1]], 'b-', linewidth=0.5)
        ax.plot([point[0], point[0] - perpendicular[0]],
                [point[1], point[1] - perpendicular[1]], color=(0, 0.3, 0.4), linewidth=0.5)
        
    elif np.pi/6 <= theta <= np.pi/2:
        phi = theta + np.pi
        point = p3
        direction = np.array([np.sin(phi), np.cos(phi)])
        perpendicular = np.array([np.cos(phi), -np.sin(phi)])
        
        ax.plot(point[0], point[1], 'ro', markersize=10)
        ax.plot([point[0] - 10*direction[0], point[0] + 10*direction[0]],
                [point[1] - 10*direction[1], point[1] + 10*direction[1]], 'b-', linewidth=0.5)
        ax.plot([point[0] - 10*direction[0] - perpendicular[0], point[0] + 10*direction[0] - perpendicular[0]],
                [point[1] - 10*direction[1] - perpendicular[1], point[1] + 10*direction[1] - perpendicular[1]], 'b-', linewidth=0.5)
        ax.plot([point[0], point[0] - perpendicular[0]],
                [point[1], point[1] - perpendicular[1]], color=(0, 0.3, 0.4), linewidth=0.5)
    
    # Устанавливаем пределы графика
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title(f'Theta: {theta:.2f}')
    plt.show()

# Пример использования
theta_values = np.linspace(-np.pi/6, np.pi/2, 10)
for theta in theta_values:
    graphics(theta)