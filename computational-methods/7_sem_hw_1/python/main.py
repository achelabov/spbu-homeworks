import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
from joblib import Parallel, delayed
import time
import math

# Вариант 7
# Определяем функции для уравнения -y'' + (e^{-x})y = x - x^2
def p(x):
    return 1  # Коэффициент при y

def r(x):
    return np.exp(-x)  # Коэффициент при y

def f(x):
    return x - x**2  # Правая часть уравнения

def q(x):
    return 0  # Не используется в данной задаче

# Метод прогонки
def tridiagonal_matrix_algorithm(K, F, N):
    start_time = time.time()
    s = np.zeros(N - 2)
    t = np.zeros(N - 1)
    y = sp.lil_matrix((N - 1, 1))

    s[0] = -K[0, 1] / K[0, 0]
    t[0] = F[0, 0] / K[0, 0]

    for i in range(1, N - 2):
        s[i] = -K[i, i + 1] / (K[i, i] + K[i, i - 1] * s[i - 1])

    for i in range(1, N - 1):
        t[i] = (F[i, 0] - K[i, i - 1] * t[i - 1]) / (K[i, i] + K[i, i - 1] * s[i - 1])

    y[N - 2, 0] = t[N - 2]

    for i in range(N - 3, -1, -1):
        y[i, 0] = s[i] * y[i + 1, 0] + t[i]

    work_time = time.time() - start_time
    return y, work_time

# Метод Якоби
def jacoby_method(K, G, err, maxNum, N, sigma):
    start_time = time.time()
    u_new = sp.lil_matrix((N - 1, 1))
    D = sp.diags(K.diagonal()).power(-1)
    u_old = sp.lil_matrix((N - 1, 1))

    for _ in range(maxNum):
        u_old = u_new.copy()
        u_new = u_old - sigma * D.dot(K.dot(u_old) - G)

        if np.linalg.norm(u_new.toarray() - u_old.toarray()) < err:
            break

    work_time = time.time() - start_time
    return u_new, work_time

# Формируем матрицу коэффициентов
def get_coef_matrix(p, r, f, N):
    h = 1 / N
    B = np.zeros(N - 1)
    A = np.zeros(N - 2)
    K = sp.lil_matrix((N - 1, N - 1))
    F = sp.lil_matrix((N - 1, 1))

    for i in range(N - 1):
        F[i, 0] = f(i*h + h) * h
        B[i] = (2 / 3) * r(i*h + h) * h + (p(i*h + (0.5 * h)) + p(i*h + (1.5 * h))) / h

    for i in range(N - 2):
        A[i] = (1 / 6) * r(i*h + (1.5 * h)) * h + -p(i*h + (1.5 * h)) / h

    K.setdiag(B)
    K.setdiag(A, 1)
    K.setdiag(A, -1)

    return K, F

# Считаем σ (воспользуемся оценкой Фробениуса)
def get_sigma(K, N):
    h = 1 / N
    sum_of_elem = np.zeros(N - 1)
    sum_of_elem[0] = K[0, 0] + K[1, 0]

    for j in range(1, N - 2):
        sum_of_elem[j] = K[j, j] + K[j - 1, j] + K[j + 1, j]

    sum_of_elem[N - 2] = K[N - 2, N - 2] + K[N - 3, N - 2]
    return 2 / np.max(sum_of_elem)

# Метод декомпозиции
def matrix_transform(N):
    n = int(math.sqrt(N))
    C = sp.lil_matrix((N - 1, N - 1))

    for i in range(N - 1):
        C[i, i] = 1

    kn = 1
    for i in range(0, (n - 1) * (n - 1)):
        C[i, n * (n - 1) + i // (n - 1)] = kn / n
        kn += 1
        if kn == n:
            kn = 1

    kn = n - 1
    for i in range(n - 1, (n - 1) * n):
        C[i, n * (n - 1) + i // (n - 1) - 1] = kn / n
        kn -= 1
        if kn == 0:
            kn = n - 1

    return C

def decomposition_method(K, F, err, maxNum, N, sigma):
    start_time = time.time()
    n = int(math.sqrt(N))
    h = 1 / N

    # Формируем предобуславливатель
    Delta_Hh = sp.lil_matrix((N - 1, N - 1))
    Delta = sp.lil_matrix((N - 1, N - 1))

    for i in range(0, n * (n - 1)):
        Delta[i, i] = 2

    for i in range(0, n * (n - 1) - 2):
        Delta[i, i + 1] = -1
        Delta[i + 1, i] = -1

    Delta /= h

    for i in range(n * (n - 1), n * n - 1):
        Delta_Hh[i, i] = 2

    for i in range(n * (n - 1), n * n - 2):
        Delta_Hh[i, i + 1] = -1
        Delta_Hh[i + 1, i] = -1

    Delta_Hh /= (h * n)
    Delta_Hh += Delta

    p_arr = np.array([p(i * (1 / 100)) for i in range(101)])
    p_mean = np.mean(p_arr)
    Delta_Hh *= p_mean

    # Матрица преобразования
    C = matrix_transform(N)
    KDD = C.transpose().dot(K.dot(C))
    FDD = C.transpose().dot(F)

    u_new = sp.lil_matrix((N - 1, 1))
    u_old = sp.lil_matrix((N - 1, 1))
    counter = 0

    for _ in range(maxNum):
        u_old = u_new.copy()
        counter += 1
        d_k = KDD.dot(u_old) - FDD

        # Применяем метод прогонки
        w_k, _ = tridiagonal_matrix_algorithm(Delta_Hh, sigma * d_k, N)
        u_new = u_old - w_k

        if np.linalg.norm(u_new.toarray() - u_old.toarray()) < err:
            break

    u_new = C.dot(u_new)
    work_time = time.time() - start_time
    return u_new, work_time, counter

# Основная часть программы
def main():
    # Вызов функций
    N = int(input("Введите N: "))
    K, F = get_coef_matrix(p, r, f, N)
    sigma = get_sigma(K, N)
    y, work_time = tridiagonal_matrix_algorithm(K, F, N)
    yJ, work_timeJ = jacoby_method(K, F, 1e-4, 10000, N, sigma)

    xh = np.arange(1 / N, 1, 1 / N)

    # N1 - количество элементов в сетке для метода декомпозиции
    N1 = int(input("Введите N1: "))
    K1, F1 = get_coef_matrix(p, r, f, N1)
    yD, work_timeD, counter = decomposition_method(K1, F1, 1e-4, 10000, N1, sigma)
    xhD = np.arange(1 / N1, 1, 1 / N1)

    # Вывод таблицы значений
    print('N=', N, ':')
    print("Времена выполнения алгоритмов:")
    print("Прогонка: ", work_time)
    print("Якоби: ", work_timeJ)
    print("Декомпозиция: ", work_timeD)

    print("#".center(7), "k1".center(15), "k2".center(17), "k3".center(17), "fi".center(17))

    for i in range(1, 10):
        print('%4d %16.12f %16.12f %16.12f ' % (
            (N * i) // 10, 
            K[(N * i) // 10, (N * i) // 10], 
            K[(N * i) // 10, ((N * i) // 10) - 1], 
            K[(N * i) // 10, ((N * i) // 10) + 1]
        ), F[(N * i) // 10, 0])

    print('\n')
    
    print("x".center(3), "y(x)".center(15), "yJacoby(x)".center(15), "yDecomp(x)".center(15))

    for i in range(1, 10):
        print('%2.1f %15.12f %15.12f %15.12f ' % (
            i * 0.1, 
            y[(N * i) // 10, 0], 
            yJ[(N * i) // 10, 0], 
            yD[(N1 * i) // 10, 0]
        ))

    # Строим графики
    plt.figure(figsize=(15, 5))

    # График метода прогонки
    plt.subplot(1, 3, 1)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Метод прогонки N=' + str(N), fontsize=12, fontweight='bold')
    plt.xlabel('x', fontsize=12, color='gray')
    plt.ylabel('y(x)', fontsize=12, color='gray')
    plt.plot(xh, y.toarray(), label='Прогонка', color='blue', linewidth=2)
    plt.legend(fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # График метода Якоби
    plt.subplot(1, 3, 2)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Метод Якоби N=' + str(N), fontsize=12, fontweight='bold')
    plt.xlabel('x', fontsize=12, color='gray')
    plt.ylabel('y(x)', fontsize=12, color='gray')
    plt.plot(xh, yJ.toarray(), label='Якоби', color='orange', linewidth=2)
    plt.legend(fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # График метода декомпозиции
    plt.subplot(1, 3, 3)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Метод декомпозиции N=' + str(N1), fontsize=12, fontweight='bold')
    plt.xlabel('x', fontsize=12, color='gray')
    plt.ylabel('y(x)', fontsize=12, color='gray')
    plt.plot(xhD, yD.toarray(), label='Декомпозиция', color='green', linewidth=2)
    plt.legend(fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
