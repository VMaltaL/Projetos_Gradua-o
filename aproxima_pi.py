# -*- coding: utf-8 -*-


"""
Nome do aluno: Victoria M
     Disciplina: MAC0115  Introdução à Computação
     Exercício-Programa EP2
Escreva um programa em Python 3.x que calcula valores aproximados para π de acordo com os quatro
m´etodos descritos a seguir. Para cada um deles, seu programa deve ler um n´umero em ponto flututante,
eps, entre 0 e 1, que ser´a utilizado para controlar a precis˜ao da aproxima¸c˜ao a ser calculada.
O seu programa deve usar somente os recursos da linguagem Python 3.x vistos em aula. Mas, n˜ao utilize
listas.
          
         Este Ep foi feito apenas com conteúdo passado durante a aula ou 
    disponibilizado na página da disciplina do moodle.
"""

import math

#------------------------------------------------------------------------------
#-----------------------Definição da função F(x) ------------------------------
#------------------------------------------------------------------------------    

def f(x):
    
    if x == 1.0:
        raiz = 0
    
    else:
        raiz = math.sqrt(1.0 - x * x)

    return raiz

#------------------------------------------------------------------------------
#------Definição da Função de aproximação pelo Método dos Retângulos-----------
#------------------------------------------------------------------------------


def areaMetodoRetangulos(a, b, k):
    
    """
    
    (float, float, int) -> float
    Recebe dois números reais a e b, com a < b, e um inteiro postivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x), no 
    intervalo [a,b], calculada pelo método dos retângulos, utilizando k
    retângulos.
    
    """


    area = 0.0
    deltax = (b-a)/ k  
    i = 0

    while i < k:
        altura = f(a + deltax*i)
        area = area + altura * deltax
        i = i + 1
        
    return area
#------------------------------------------------------------------------------
#------Definição da Função de aproximação pelo Método dos Trapézios------------
#------------------------------------------------------------------------------
    
    
def areaMetodoTrapezios(a, b, k):
    
    """
    
    (float, float, int) -> float
    Recebe dois números reais a e b, com a < b, e um inteiro postivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x), no 
    intervalo [a,b], calculada pelo método dos trapézios, utilizando k
    trapézios.
    
    """


    area = 0.0
    deltax = (b-a)/ k  
    i = 1
    j = 0

    while i < k:
        soma_alturas = f(a + deltax*i) + f(a + deltax * j)
        area = area + soma_alturas/2 * deltax
        i = i + 1
        j = j + 1
    return area
   
#------------------------------------------------------------------------------
#-----Definição da Função de aproximação através da série de Wallis------------
#------------------------------------------------------------------------------


def piSerieWallis(eps):
    
    """
    (float) -> int, float
    
    Recebe um número real eps, com 0 < eps < 1.
    Esta função calcula um valor aproximado para pi, piAproxWallis, através da
    serie de Wallis, incluindo os primeiros termos até que o valor da absoluto 
    da diferença entre o valor de calculado piAproxWallis e o valor da 
    constante math.pi seja menor do que eps. A função retorna o número de 
    termos considerados e o valor calculado piAproxWallis.
    Obs.: Para determinar o valor absoluto é utilizada a função fabs do
    módulo math.
    
    """
    
    
    termos = 0
    i = 0
    j = 0
    par = 0
    impar = 0
    piAproxWallis = 2
    #começando a aproximação de 2, não será necesário criar outra variável
    
    while math.fabs(piAproxWallis - math.pi) >= eps :
        
        if i == j:
            i = i + 1
            
        else: 
            j = j + 1
            
        termos = termos + 1
        par = i * 2
        impar = j * 2 + 1
        piAproxWallis = piAproxWallis * par/impar
        
        
    return termos, piAproxWallis

#------------------------------------------------------------------------------
#-----Definição da Função de aproximação através da séria de Nilakantha--------
#------------------------------------------------------------------------------


def piSerieNilakantha(eps):
    
    """
    (float) -> int, float
    
    Recebe um número real eps, com 0 < eps < 1.
    Esta função calcula um valor aproximado para pi, piAproxNilakantha, através
    da serie de Nilakantha, incluindo os primeiros termos até que o valor da 
    absoluto da diferença entre o valor de calculado piAproxNilakantha e o 
    valor da constante math.pi seja menor do que eps. A função retorna o número
    de termos considerados e o valor calculado piAproxNilakantha.
    Obs.: Para determinar o valor absoluto é utilizada a função fabs do
    módulo math.
    
    """
    
    piAproxNilakantha = 3.0
    
    sinal = 1 
    i = 2
    while eps <= math.fabs(math.pi-piAproxNilakantha):
        termo = sinal * 4/(i *(i + 1)*(i + 2))
        sinal = sinal * -1
        piAproxNilakantha += termo  
        i += 2


    return i-1, piAproxNilakantha

#------------------------------------------------------------------------------
#---------------------Definição da função Principal----------------------------
#------------------------------------------------------------------------------

def main():
    
    print("""
-------------------------------------------------------------------------------
             ALGUMAS APROXIMAÇÕES PARA O VALOR DE PI:
             (utilizamos math.pi que é  3.141592653589793)
-------------------------------------------------------------------------------
          """)
        
        
    #intervalo para os dois primeoros métodos    
    a = 0.0
    b = 1.0
    
#--------------------Método dos retângulos------------------------------------   


    print("""
Método 1- Valor aproximado para PI utilizando o Método dos Retângulos""")
    
    
    k_1 = 1
    eps_1 = float(input("Digite um número (>0 e < 1) para epsilon: "))
    
    aproxMetodoRetangulos = 0
    while eps_1 <= math.fabs(aproxMetodoRetangulos - math.pi):
        k_1 = k_1 * 2
        aproxMetodoRetangulos = areaMetodoRetangulos(a, b, k_1) * 4
        
    print (
"\nNúmero de retângulos considerados para o cálculo da última área: ", k_1,
    
"\nValor aproximado para PI: " ,aproxMetodoRetangulos)
    
#--------------------Método dos trapézios--------------------------------------     
    
    print("""
-------------------------------------------------------------------------------
          """)
    
    print("""
Método 2- Valor aproximado para PI utilizando o Método dos Trapézios""")
    
    
    k_2 = 1
    eps_2 = float(input("Digite um número (>0 e < 1) para epsilon: "))
    aproxMetodoTrapezios = 0
    while eps_2 <= math.fabs(aproxMetodoTrapezios - math.pi):
        k_2 = k_2 * 2
        aproxMetodoTrapezios = areaMetodoTrapezios(a, b, k_2) * 4
        
    print (
"\nNúmero de trapézios considerados para o cálculo da última área: ", k_2,
    
"\nValor aproximado para PI: " ,aproxMetodoTrapezios) 
    
    print("""
-------------------------------------------------------------------------------
          """)
    
#-----------------Aproximação Série Wallis-------------------------------------
    
    
    print("""
-------------------------------------------------------------------------------
          """)
    
    print("""
Método 3- Valor aproximado para PI utilizando a série de Wallis""")   
     
    eps_3 = float(input("Digite um número (>0 e < 1) para epsilon: "))
    
    a = piSerieWallis(eps_3)
    
    print("\nNúmero de termos da série incluídos no cálculo:", a[0],
          "\nValor aproximado para PI:", a[1])
    
    print("""
-------------------------------------------------------------------------------
          """)
#-----------------Aproximação Série Nilatankha---------------------------------
    
    
    print("""
-------------------------------------------------------------------------------
          """)
    
    print("""
Método 4- Valor aproximado para PI utilizando a série de Nilakantha""")        
    
    eps_4 = float(input("Digite um número (>0 e < 1) para epsilon: "))
    b = piSerieNilakantha(eps_4)
    
    print("\nNúmero de termos da série incluídos no cálculo:", b[0],
          "\nValor aproximado para PI:", b[1])
    
    print("""
-------------------------------------------------------------------------------
          """)
#------------------------------------------------------------------------------
#---------------------Chama a função Principal---------------------------------
#------------------------------------------------------------------------------
main()