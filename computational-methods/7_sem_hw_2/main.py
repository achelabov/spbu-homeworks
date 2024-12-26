
import numpy as np 
import pandas as pd

def progonka (K1, K2, K3, f): 
    N = K2.shape[0] 
    u_prog = np.zeros(N) 
    alpha = np.zeros(N+1)
    beta = np.zeros(N+1)
    alpha [0] = -K3[0]/K2[0]
    beta[0] = f[0]/K2[0]
    for i in range(N-1):
        alpha[i+1] = -K3[i]/(K2[i]+alpha[i]*K1[i])
        beta[i+1] = (-K1[i]*beta[i]+f[i])/(K2[i]+alpha[i]*K1[i])
    u_prog[N-1] = beta [N-1]
    for i in range(N-2, -1, -1):
        u_prog[i] = alpha[i+1]*u_prog[i+1]+beta[i+1]
    return u_prog

def yavnaya(h, tau, phi, alpha, beta, f, U):
    x = np.arange(0, 1+h, h)
    t = np.arange(0, 0.1+tau, tau)
    M = t.shape[0]
    N = x.shape[0]
    u = np.zeros((N,M))
    for i in range (N):
        u[i][0] = phi(x[i])
    for k in range(M-1):
        for j in range(1,N-1):
            Lh = (u[j+1][k] -2*u[j][k]+u[j-1] [k])/h**2 
            u[j][k+1] = u[j][k] + tau*(Lh + f(x[j],t[k]))
    for k in range (M):
        u[0][k] = alpha(t[k])
        u[N-1] [k] = 1/3*(4*u[N-2][k] -u[N-3] [k]+2*h*beta(t[k]))
    err = np.zeros((N,M))
    for k in range (M):
        for j in range (N):
          err[j][k] = u[j][k] - U(x[j], t[k])
    max_err = max([np.max([np.abs (item) for item in e]) for e in err])
    return u, max_err


def neyavnaya(h, tau, phi, alpha, beta, f, U, sigma):
    x = np.arange(0, 1+h, h)
    t = np.arange(0, 0.1+tau, tau)
    M = t.shape[0]
    N = x.shape[0]
    u = np.zeros((N,M))
    u_ex = np.zeros((N,M))
    for i in range (N):
        u[i][0] = phi(x[i])
    A = np. zeros (N) 
    B = np.zeros(N)
    C = np. zeros (N) 
    G = np.zeros(N) 
    B[0] = 1
    B[N-1] = 1
    for k in range(1,M):
        G[0] = alpha(t[k]) 
        G[N-1] = beta(t[k])
        for j in range(1,N-1):
            Lh = (u[j+1][k-1] -2*u[j] [k-1]+u[j-1] [k-1])/h**2
            G[j] = u[j][k-1] + tau* (1-sigma) *Lh+tau*f(x[j],t[k]) 
            A[j] = sigma*(-tau/h**2)
            B[j] = 1+(sigma*2*tau/h**2)
            C[j] = sigma*(-tau/h**2)
        for i in range(len(u)):
            u[i] [k] = progonka (A, B, C, G) [i]
    for k in range (M):
        u[0][k] = alpha(t[k])
        u[N-1] [k] = 1/3*(4*u[N-2] [k] -u [N-3] [k]+2*h*beta(t[k]))
    for k in range (M):
        for j in range (N):
            u_ex[j][k] = U(x[j],t[k])
    diff = [np.abs(u_ex[i]-u[i]) for i in range(len(u))]
    return u

def u_ex (x,t):
    return x**3+t**3
def f(x,t):
    return x**4 - 9*x**2 + 3*t**2 + x*t**3 - 18*x
def phi(x):
    return x**3
def alpha(x):
    return 3*x**2
def beta(t):
    return 1+ t**3

def main (N, sigma):
    tau = (1/N)**2/4
    M=int(round (0.1/((1/N) **2/4)))
    h = 1/N
    u_yavnaya, yavn_err=yavnaya(h, tau, phi, alpha, beta, f,u_ex) 
    u_neyavnaya=neyavnaya(h, tau, phi, alpha, beta, f, u_ex, sigma)
    u_f_yavnaya=np.zeros((6,6)) 
    u_f_neyavnaya=np.zeros((6,6))
    for k in range(6):
        for j in range(6):
            u_f_yavnaya[j][k]=u_yavnaya[int(N*j/5)][int(k*M/5)]
            u_f_neyavnaya[j][k]=u_neyavnaya [int (j*N/5)][int (k*M/5)]
    u_f_yavnaya=u_f_yavnaya.T
    u_f_neyavnaya=u_f_neyavnaya.T
    return u_yavnaya, yavn_err, u_neyavnaya, u_f_yavnaya, u_f_neyavnaya

N = 20
sigma = 1
u_yavnaya, yavn_err, u_neyavnaya,  u_f_yavnaya, u_f_neyavnaya = main (N, sigma)
diff = [u_f_yavnaya[i]-u_f_neyavnaya[i] for i in range(len(u_f_yavnaya))]
table_yavnaya = pd.DataFrame([row for row in u_f_yavnaya], columns = [0, 0.2, 0.4, 0.6, 0.8, 1], 
                             index = [0, 0.02, 0.04, 0.06, 0.08, 1]) 
table_neyavnaya = pd.DataFrame([row for row in u_f_neyavnaya], columns = [0, 0.2, 0.4, 0.6, 0.8, 1], 
                               index = [0, 0.02, 0.04, 0.06, 0.08, 1])
print(f"Результаты вычислений для явной схемы с N = {N}")
print(table_yavnaya)
print(f"Результаты вычислений для неявной схемы с N = {N}, sigma = {sigma}")
print(table_neyavnaya)
