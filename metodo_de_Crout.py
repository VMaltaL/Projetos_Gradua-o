# Feito por Victoria M

import numpy as np

#-----------------------------------------------------------------------------
def main():
    
    print ("""
           Este programa usa a decomposição LU para construir um método,
           (método de Crout) que permite resolver de maneira eficiente sistemas
           lineares dados por matrizes tridiagonais. 
           Como aplicação construiremos splines cúbicos e resolveremos algumas
           equações diferenciais pelo método de diferenças finitas.
           
           
           Temos duas opções para esse programa: 
            A opção 1 é o método de Crout com uma matriz simples
            e a opção 2 é a aplicação do método trabalhado na opção 1.""")
           
           
    opcao = int(input("Digite '1' para opção 1 e '2' para a opção 2: "))
    
    
    #variaveis
    a =[[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]]
    n = len (a[0]) - 1

    
    
    if opcao == 1:
        
        metCrout(a, n)
        
    elif opcao == 2:
        aplicacao()
        
    
#-----------------------------------------------------------------------------
def metCrout(a, n):
    # decompoe a matriz a, tridiagonal, em duas matrizes (l e u)
    # calcula as soluções para um vetor y, usando as matrizes criadas
    
    #variaveis
    l = np.zeros([n+1,n+1])
    u = np.zeros([n+1,n+1])
    z = np.zeros(n+1)
    x = np.zeros(n+1)
    y = [1,0,0,1]
    #decompõe A em L e U 
    l[0][0] = a[0][0]
    u[0][1] = a[0][1] / l[0][0]
    for i in range(0, n):
        l[i][i-1] = a[i][i-1]
        l[i][i] = a[i][i] - l[i][i-1] * u[i-1][i]
        u[i][i+1] = a[i][i+1]/l[i][i]
        u[i][i] = 1
    
    l[n][n-1] = a[n][n-1]
    l[n][n] = a[n][n] - l[n][n-1] * u[n-1][n]
    u[n][n] = 1
    
    
    #criando a matriz Z
    z[0] = y[0]/l[0][0]
    
    for i in range(1, n+1):
        z[i] = (y[i] - l[i][i-1] * z[i-1])/ l[i][i] 
        
        
        
    #calculando x
    x[n] = z[n]
    
    for i in range(n-1, -1, -1):
        x[i]= z[i] - u[i][i+1] * x[i+1]
        
    imprime_metCrout(a, l, u, z, x)
#------------------------------------------------------------------------------

def imprime_metCrout(a, l, u, z, x):      
    print('\n')
    #imprime as matrizes 
    a = np.array(a)
    print('\n A matriz original é:') 
    print(a)
    
    l = np.array(l)
    print('\n A matriz L gerada é:')
    print(l)
    
    u = np.array(u)
    print('\n A matriz U gerada é:')
    print(u)
    
    z = np.array(z)
    print('\n A matriz Z gerada é:')
    print(z)
    
    x = np.array(x)
    print('\n A matriz X gerada é:')
    print(x)

#------------------------------------------------------------------------------
def aplicacao():
    
    print("Essa função ainda esta sendo criada!")
    
    
#------------------------------------------------------------------------------
main()
