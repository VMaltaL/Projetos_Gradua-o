# -*- coding: utf-8 -*-
# Feito por Victoria M

import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return (-(20*x)+10)/(10+(10*(x-(1/2))**2))

def r(x):
    
    return 0

def q(x):
    
    return 0

def criaVetorX(n, x0, h):
    #cria vetor com zeros    
    x = np.zeros(n)
    #altera com os x2 a xn-1, com intervalo h
    for i in range(0, n+1):
        x[i-1] = x0 + i* h
       
    return x

def criaMatrizA(n,x, h):
    #cria matriz com zeros
    a = np.zeros([n,n])
    #altera a diagonal principal 
    for i in range(0, n):
        a[i][i] = 2+(q(x[i])*(h**2))
    #altera as diagonais inferior e superior   
    for i in range(1,n):
        #diagonal inferior
        a[i][i-1] = -1-((h/2)*p(x[i]))
    for i in range(n-1):    
        #diagonal superior
        a[i][i+1] = -1+((h/2)*p(x[i]))

    return a

def criaVetorB(n,x, h, alpha, beta):
    
    b = np.zeros(n)
    b[0] = -r(x[0])*(h**2) + ((1 + h/2 * p(x[0])) * alpha)
    b[n-1] = -r(x[n-1])*(h**2) +((1 - h/2 * p(x[n-1]))*beta)
    for i in range(1,n-1):
        b[i]=-r(x[i])*(h**2)

    return b

def metCrout(a, n, b, alpha,beta):
    # decompoe a matriz a, tridiagonal, em duas matrizes (l e u)
    # calcula as soluções para um vetor y, usando as matrizes criadas
    
    
    n = n-1 #atualiza n para o método de crout
    l = np.zeros([n+1,n+1])
    u = np.zeros([n+1,n+1])
    z = np.zeros(n+1)
    w = np.zeros(n+1)

    #decompõe A em L e U 
    l[0][0] = a[0][0]
    u[0][1] = a[0][1] / l[0][0]
    for i in range(1, n):
        l[i][i-1] = a[i][i-1]
        l[i][i] = a[i][i] - l[i][i-1] * u[i-1][i]
        u[i][i+1] = a[i][i+1]/l[i][i]
        
    for i in range(0, n+1):
        u[i][i] = 1
    
    l[n][n-1] = a[n][n-1]
    l[n][n] = a[n][n] - l[n][n-1] * u[n-1][n]
    
    
    #criando a matriz Z
    z[0] = b[0]/l[0][0]
    
    for i in range(1, n+1):
        z[i] = (b[i] - l[i][i-1] * z[i-1])/ l[i][i] 
        
        
        
    #calculando x
    w[n] = z[n]
    
    for i in range(n-1, -1, -1):
        w[i]= z[i] - u[i][i+1] * w[i+1]
    #adiciona os valores de x1 e xn
    n = n+1
    w = np.insert(w,0,alpha)
    w = np.insert(w,n+1,beta)
    #imprime w 
    w = np.array(w)
    print('\nO vetor w gerado é:')
    print(w)   
    return w

def imprimeGraf(x0,xn,n,w):
    t = np.linspace(x0, xn, n+2)
    plt.plot(t,w)
    plt.show()

def calculoMediaTemp(n,w,h,xn):
    
    integral = (h/2)*(w[0]+w[n+1])
    
    for i in range(1,n+1):
        integral = integral + h * w[i]
        
    temp_med = integral/xn
        
    print ("\nO valor da média da temperatura da barra é:", temp_med, end=".")

def main():
    
    print("""Este programa calcula os wi de uma matriz W, com dados x inicial 
e final e seu respectivo espaçamento dado pelo número de divisões desejadas
(neste caso, se refere a dados de uma barra) e gera um gráfico de
x por w. Calcula também a media da temperatura da barra pelo método do Trapézio""")
    #dados do problema      
    n = 49 #divisões
    x0 = 0 #x inicial(a)
    xn = 2 #x final (b)
    alpha = 20 # w(a)
    beta = 30 #w(b)
    h = (xn-x0)/(n+1) #espaçamento dos x
    
    
    x = criaVetorX(n, x0, h)   
    a = criaMatrizA(n,x, h)
    b = criaVetorB(n,x, h, alpha, beta)
    w = metCrout(a, n, b,alpha,beta)
    imprimeGraf(x0,xn,n,w)
    calculoMediaTemp(n,w,h,xn)

main()
