import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import math
import pandas as pd
from scipy.optimize import fmin
from typing import Callable


H = lambda x, y: np.exp(x * y)
f = lambda x: x+ .5
a, b = 0, 1
# Метод замены ядра на вырожденное
def taylor(k):
    return lambda x: x**k / np.sqrt(math.factorial(k))

alpha = [taylor (k) for k in range(4)]
beta = [taylor (k) for k in range(4)]
H_3 = lambda x, y: np. sum( [alpha[i] (x) * beta[i] (y) for i in range(3)]) 
# H_4 = lambda x, y: np. sum( [alpha[i] (x) * beta[i] (y) for i in range(4)])
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(5, 5), dpi=200)
# X = np.linspace(a, b, 100)
# Y = np.linspace (a, b, 100) 
# X, Y = np.meshgrid(X, Y)
# Z_1 = np.exp(X * Y)
# Z_2 = taylor(0)(X) * taylor(0)(Y) + taylor(1)(X) * taylor(1)(Y) + taylor(2)(X) * taylor(2)(Y)
# surf = ax.plot_surface (X, Y, Z_1, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.7) 
# surf = ax.plot_surface (X, Y, Z_2, cmap=cm. viridis, linewidth=0, antialiased=True, alpha=0.7) 
# ax.invert_yaxis()
# ax.invert_xaxis()
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()

# ---------------------------------------------------------------------------------------------

def taylor(k):
    return lambda x: x**k / np.sqrt(math.factorial(k))

alpha = [taylor(k) for k in range(4)]
beta = [taylor(k) for k in range(4)]

def B(k):
    res = np.zeros(k)
    for i in range(k):
        res[i], _ = quad(lambda x: beta[i](x) * f(x), a, b)
    return res

def G(k):
    res = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            res[i][j], _ = quad(lambda x: beta[i](x) * alpha[j](x), a, b)
    return res

def A(k):
    G_k = G(k)
    res = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            res[i][j] = (i == j) - G_k[i][j]
    return res

def C(k):
    return np.linalg.solve(A(k), B(k))

# # Вывод результатов
# print("A(3) = ", A(3), "\nB(3) = ", B(3), "\nC(3) = ", C(3))
# print("A(4) = ", A(4), "\nB(4) = ", B(4), "\nC(4) = ", C(4))


# Функция для форматированного вывода матриц
def print_matrix(matrix, name):
    print(f"{name} = ")
    for row in matrix:
        print("  [", "  ".join(f"{val:.6f}" for val in row), "]")
    print()

# Вывод результатов
print_matrix(A(3), "A(3)")
print_matrix(B(3).reshape(1, -1), "B(3)")
print_matrix(C(3).reshape(1, -1), "C(3)")

print_matrix(A(4), "A(4)")
print_matrix(B(4).reshape(1, -1), "B(4)")
print_matrix(C(4).reshape(1, -1), "C(4)")

# ---------------------------------------------------------------------------------------------

def U(k):
    C_k = C(k)
    return lambda x: f(x) + sum(C_k[i] * alpha[i](x) for i in range(k))

u_3 = U(3)
u_4 = U(4)

pts = [0, 0.5, 1]

# Вычисление максимальной разности
delta = np.max([abs(u_3(p) - u_4(p)) for p in pts])
print(f"Delta = {delta}")

# Создание DataFrame
data = {
    "U3": {
        "0": u_3(0),
        "0.5": u_3(0.5),
        "1": u_3(1)
    },
    "U4": {
        "0": u_4(0),
        "0.5": u_4(0.5),
        "1": u_4(1)
    }
}

df = pd.DataFrame(data)
print(df)

# ---------------------------------------------------------------------------------------------

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

x = np.linspace(a, b, 100)

plt.plot(x, u_3(x), color='red', label=r'$u_3$', alpha=0.8)
plt.plot(x, u_4(x), color='blue', label=r'$u_4$', alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()

plt.show()

# ---------------------------------------------------------------------------------------------

# Оптимизация
norm = lambda x: -abs(u_3(x) - u_4(x)) if a <= x <= b else 0
fmin_result = fmin(norm, 0)

def D(k):
    return np.linalg.inv(A(k))

def Res(x, y, k=3):
    s = 0
    D_ = D(k)
    for i in range(k):
        for j in range(k):
            s += D_[i][j] * alpha[i](x) * beta[j](y)
    return s

IRes = lambda x: abs(quad(lambda y: Res(x, y), a, b)[0])

# Построение графиков
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

x = np.linspace(a, b, 100)

plt.plot(x, [IRes(p) for p in x], color='red', label=r'$\int_0^1 | \tilde{G}(x, y) | dy$')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()

plt.show()

# ---------------------------------------------------------------------------------------------

# Вычисление интеграла от остаточной функции
M = IRes(b)
print(f"\\tilde{{B}} = {M}")

def Ker(x, y):
    return abs(H(x, y) - H_3(x, y))

IKer = lambda x: quad(lambda y: Ker(x, y), a, b)[0]

# Построение графиков
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

x = np.linspace(a, b, 100)

plt.plot(x, [IKer(p) for p in x], color='red', label=r'$\int_0^1 | H(x, y) - \tilde{H}(x, y) | dy$')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()

plt.show()

# ---------------------------------------------------------------------------------------------

# Вычисление значений eta и M
eta = IKer(b)
print(f"η = {eta}")

# # Вычисление относительной ошибки
# relative_error = np.abs(u_3(x) - u_4(x)) / (1 + M) * eta / (1 - (1 + M) * eta)
# print(f"Relative error: {relative_error}")

# Построение графиков
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

x = np.linspace(a, b, 100)

plt.plot(x, np.abs(u_3(x) - u_4(x)), color='red', label=r'$|u_3 - u_4|$')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()

plt.show()

# ---------------------------------------------------------------------------------------------

# Метод механических квадратур

n = 200
eps = 1.e-8

def target(u: Callable) -> float:
    return abs(max(u(a), u((a + b) / 2), u(b)))

var = 1.e+8
u_n = u_3

while var > eps:
    n *= 2
    h = (b - a) / (n + 1)
    x_ = np.linspace(a + h, b - h, n)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i][j] = (i == j) - h * H(x_[i], x_[j])
    
    q = f(x_)
    z = np.linalg.solve(D, q)
    t_prev = target(u_n)

    def sol(x):
        s = f(x)
        for i in range(n):
            s += h * H(x, x_[i]) * z[i]
        return s

    u_n = sol
    t_next = target(u_n)
    var = abs(t_prev - t_next)

n = 800

fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
x = np.linspace(a, b, 100)
plt.plot(x, u_3(x), color="red", label=r"$u_3$", alpha=0.8)
plt.plot(x, u_4(x), color="blue", label=r"$u_4$", alpha=0.8)
plt.plot(x, u_n(x), color="green", label=r"$u_n$", alpha=0.8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid()
plt.show()
