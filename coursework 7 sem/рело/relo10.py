import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation

# Определяем точки
p1 = np.array([np.sqrt(3)/4, 0])
p2 = np.array([-np.sqrt(3)/4, -0.5])
p3 = np.array([-np.sqrt(3)/4, 0.5])

ps = [p1, p2, p3]

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
    
    return []

# Создаем значения theta
theta_values = np.concatenate((np.linspace(-np.pi/6, np.pi/2, 100), np.linspace(np.pi/2, -np.pi/6, 100)))

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=len(theta_values), init_func=init, blit=False, repeat=True)

# Отображаем анимацию
plt.show()