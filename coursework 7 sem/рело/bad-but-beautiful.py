import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Параметры анимации
interval = 50  # ms, время между кадрами анимации

# Создание фигуры и осей
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.15, bottom=0.35)
ax.set_aspect('equal')
plt.xlim(-1.4 * 8, 1.4 * 8)
plt.ylim(-1.4 * 8, 1.4 * 8)

# Инициализация элементов для отображения
inner_pin, = ax.plot([0], [0], 'g-')  # Внутренний шарнир
d0, = ax.plot([0], [0], 'r-')         # Центральный круг
dot, = ax.plot([0], [0], 'ro', ms=5)   # Точка на внутреннем шарнире

# Функция для обновления внутреннего шарнира
def update_inner_pin(Rm, rm, rc, phi):
    t = np.linspace(0, 2 * np.pi, 2000)
    e = rm - rc
    x = (Rm + e) * np.cos(t) + e * np.cos(phi)
    y = (Rm + e) * np.sin(t) + e * np.sin(phi)
    inner_pin.set_data(x, y)
    
    x1 = (Rm) * np.cos(t) * np.cos(phi) - (Rm) * np.sin(t) * np.sin(phi)
    y1 = (Rm) * np.cos(t) * np.sin(phi) + (Rm) * np.sin(t) * np.cos(phi)
    d0.set_data(x1, y1)
    dot.set_data([x1[0]], [y1[0]])

# Функция для обновления циклоиды
cycloidA, = ax.plot([0], [0], 'b-')
def update_cycloidA(rm, rc, R):
    t = np.linspace(0, rm * 2 * np.pi, 2000)
    e = rm - rc
    x = e * np.cos(t) + R * np.cos((rm - rc) / rm * t)
    y = e * np.sin(t) + R * np.sin((rm - rc) / rm * t)
    cycloidA.set_data(x, y)

# Инициализация элементов для отображения треугольника Рело
num_arcs = 3
arcs = [ax.plot([], [], 'g-')[0] for _ in range(num_arcs)]
dotR, = ax.plot([0], [0], 'go', ms=5)

# Функция для инициализации треугольника Рело
def draw_Reuleaux_init():
    for p in arcs:
        p.set_data([0], [0])

# Функция для обновления треугольника Рело
def update_reuleaux_triangle(n, rm, rc, R, phi):
    e = rm - rc
    R_reuleaux = (rm - rc) / np.sqrt(3)  # Радиус окружностей треугольника Рело
    
    for i in range(n):
        t = np.linspace(0, 2 * np.pi / 3, 2000)
        xa = R_reuleaux * np.cos(t)
        ya = R_reuleaux * np.sin(t)
        
        x = xa * np.cos(i * 2 * np.pi / n + phi) - ya * np.sin(i * 2 * np.pi / n + phi) + e * np.cos(phi)
        y = xa * np.sin(i * 2 * np.pi / n + phi) + ya * np.cos(i * 2 * np.pi / n + phi) + e * np.sin(phi)
        arcs[i].set_data(x, y)
        if i == 0:
            dotR.set_data([x[0]], [y[0]])

# Создание слайдеров для управления параметрами
axcolor = 'lightgoldenrodyellow'
ax_fm = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_rc = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_rm = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_R = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 80, valinit=40, valstep=1)
sli_Rm = Slider(ax_Rm, 'Rm', 0.5, 40, valinit=8, valstep=0.1)
sli_rc = Slider(ax_rc, 'rc', 1, 20, valinit=2, valstep=0.1)
sli_rm = Slider(ax_rm, 'rm', 1, 20, valinit=10, valstep=0.1)
sli_N = Slider(ax_N, 'N', 2, 5, valinit=3, valstep=1)
sli_R = Slider(ax_R, 'R', 1, 80, valinit=16, valstep=0.1)

# Функция для обновления параметров при изменении слайдеров
def update(val):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    src = sli_rc.val
    srm = sli_rm.val
    sN = sli_N.val
    sR = sli_R.val
    ax.set_xlim(-1.4 * sR, 1.4 * sR)
    ax.set_ylim(-1.4 * sR, 1.4 * sR)

sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_rc.on_changed(update)
sli_rm.on_changed(update)
sli_N.on_changed(update)
sli_R.on_changed(update)

# Кнопка для сброса параметров
resetax = plt.axes([0.86, 0.02, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()
    sli_Rm.reset()
    sli_rc.reset()
    sli_rm.reset()
    sli_N.reset()
    sli_R.reset()

button.on_clicked(reset)

# Функция для анимации
def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    src = sli_rc.val
    srm = sli_rm.val
    sN = sli_N.val
    sR = sli_R.val
    frame += 1
    phi = 2 * np.pi * frame / sfm
    update_inner_pin(sRm, srm, src, phi)
    update_cycloidA(srm, src, sR)
    draw_Reuleaux_init()
    update_reuleaux_triangle(sN, srm, src, sR, phi)
    fig.canvas.draw_idle()

# Запуск анимации
ani = animation.FuncAnimation(fig, animate, frames=sli_fm.val * sli_N.val * int(sli_fm.val / 10), interval=interval)
plt.show()