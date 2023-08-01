# -*- coding: utf-8 -*-
"""
Nome do aluno: Victoria M
     Disciplina: MAC0115  Introdução à Computação
     Exercício-Programa EP3

        Escreva um programa em Python 3.x para resolver trˆes problemas, de forma independente. Esses trˆes
problemas utilizam o Crivo de Erat´ostenes, direta ou indiretamente.
Algoritmo do Crivo de Erat´ostenes
No s´eculo trˆes A.C., o matem´atico e astrˆonomo grego Erat´ostenes desenvolveu um algoritmo para determinar
todos os n´umeros primos at´e um dado n´umero inteiro positivo n. Esse algoritmo ´e chamado de Crivo de
Erat´ostenes. (Implementa¸c˜oes deste algoritmo foram dadas numa das aulas.)
Veja na p´agina Crivo de Erat´ostenes na Wikip´edia uma anima¸c˜ao desse algoritmo
(https://pt.wikipedia.org/wiki/Crivo de Erat´ostenes).
PROBLEMA 1:
Dado um inteiro positivo n, n ≥ 2, determinar todos os n´umeros primos menores ou iguais a
n, utilizando o Crivo de Erat´ostenes.
A sua solu¸c˜ao deve utilizar as seguintes fun¸c˜oes, cujos prot´otipos est˜ao definidos mais adiante:
criaListaCrivoEratostenes, criaListaPrimos e imprimeNumerosInteirosLista.
Deve imprimir a quantidade de primos e os n´umeros primos encontrados.
PROBLEMA 2:
Dado um inteiro positivo n, n > 2, encontrar uma sequˆencia consecutiva mais longa de inteiros
menores do que n sem nenhum n´umero primo. Ou seja, determinar um par de n´umeros primos
r e s tais que 2 ≤ r < s ≤ n, o valor da diferen¸ca s − r ´e m´aximo e para todo inteiro i tal que
r < i < s, tem-se que i n˜ao ´e primo. Basta encontrar um tal par (n˜ao precisa encontrar todos
tais pares).
A sua solu¸c˜ao deve utilizar a fun¸c˜ao maiorIntervaloSemPrimos, cujo prot´otipo est´a definido mais adiante e
escrever uma mensagem clara sobre os primos r e s encontrados com rela¸c˜ao a n e a quantidade de n´umeros
n˜ao primos entre r e s.
PROBLEMA 3:
Em 1742, Christian Goldbach conjecturou que todo n´umero par maior do que 2 pode ser escrito como
soma de dois n´umeros primos. Por exemplo, 16 = 3 + 13.
A Conjectura de Goldbach ainda n˜ao foi resolvida, mas sabe-se que ela ´e verdadeira para todo inteiro par n
tal que n < 1014
.
Dado um inteiro k > 2, verificar se a Conjectura de Goldbach ´e verdadeira para todo inteiro
par n tal que 2 < n < k. Para isto, para cada tal inteiro n, encontrar dois n´umeros primos p
e q tais que n = p + q. Veja mais adiante especifica¸c˜oes mais detalhadas a respeito de p e q.
A sua solu¸c˜ao deve utilizar a fun¸c˜ao testaConjecturaGoldbach, cujo prot´otipo est´a definido mais adiante.
Esta fun¸c˜ao fornece tamb´em um certificado (para cada n, fornece o valor de p, onde p, q ´e um par de
primos tais que n = p + q).
  
         Este Ep foi feito apenas com conteúdo passado durante a aula ou 
    disponibilizado na página da disciplina do moodle.
"""


import math

#------------------------------------------------------------------------------
#---------------------Definição da função Principal----------------------------
#------------------------------------------------------------------------------

def main():
    """
    
    ( ) -> NoneType
    
    Chama as funções resolveProblema1, resolveProblema2 e resolveProblema3.
    
    """
    resolveProblema1()
    resolveProblema2()
    resolveProblema3()
    
#------------------------------------------------------------------------------
#-------------------Definição da resolveProblema1() ---------------------------
#------------------------------------------------------------------------------

def resolveProblema1():
    
    """
    
    ( ) -> NoneType
    
    Chama as funções criaListaCrivoEratostenes, criaListaPrimos e
    imprimeNúmerosInteiros com o valor de entrada n dado pelo usuário,
    imprime os resultados para o problema 1 seguindo o formato adequado.
    
    """
    
    
    print("\n\nPROBLEMA 1")
    print("\nDetermina números primos menores ou iguais a n.")
    n = int(input("Digite um inteiro >= 2 para n: "))
    a = criaListaCrivoEratostenes(n)
    b = criaListaPrimos(a)
    print("\nExistem %d números primos menores ou iguais a %d. São eles:\n" 
          %(len(b),len(a)-1))
    imprimeNumerosInteiros(b)
    
    
    print(
"\n\n===============================================================")
    

#------------------------------------------------------------------------------
#-------------------Definição da resolveProblema2() ---------------------------
#------------------------------------------------------------------------------
def resolveProblema2():
    
    """
    
    ( ) -> NoneType
    
    Chama a função maiorIntervaloSemPrimos com o número de entrada n dado pelo
    usuário, imprime o resultado para o problema 2 seguindo o formato adequado.
    """
    
    
    print("\n\nPROBLEMA 2")
    print("""
Determinar dois números primos r e s tais que 2 <= r < s <= n,
o valor de s−r é máximo e não existem números primos entre r e s.""")
    
    n = int(input("Digite um inteiro >= 2 para n: "))
    
    a = maioriIntervaloSemPrimos(n)
    
    
    print("""
Uma sequência consecutiva mais longa de inteiros menores do que %d,
sem nenhum número primo, é formada por %d inteiros que estão entre 
o par de números primos %d e %d.""" %(n,a[1]-a[0]-1,a[0], a[1]))
    print(
"\n\n===============================================================")
    
    
#------------------------------------------------------------------------------
#-------------------Definição da resolveProblema3() ---------------------------
#------------------------------------------------------------------------------
def resolveProblema3(): 
    
    """ ( ) -> NoneType
    
    Chama a função testaConjecturaGoldbach com o número de entrada k dado pelo
    usuário, imprime o resultado para o problema 3 seguindo o formato adequado.
    """
    
    
    print("\n\nPROBLEMA 3")
    print("\nTestar a Conjetura de Goldbach para todo inteiro par menor do que k.")
    k = int(input("\nDigite um inteiro > 4 para k: "))
    a = testaConjecturaGoldbach(k)
    pares_primos = a[0]
    
    print(
"\nPara todo n par tal que 2 < n < 120, os pares p e q tais que n = p + q são:\n")
    if a[1]:
        for i in range(2,len(pares_primos)):
            print("%6d = %4d + %4d" 
                  %(2 * i,pares_primos[i],(i*2)-pares_primos[i]))
    else:
        print("A conjectura não vale para esse k.")
        
    print(
"\n\n===============================================================")    
#------------------------------------------------------------------------------
#------------Definição da função criaListaCrivoEratostenes(n) -----------------
#------------------------------------------------------------------------------

def criaListaCrivoEratostenes(n):
    
    """ 
    (int) -> list
    Recebe um inteiro positivo n, n >= 2, e cria uma lista crivo[0...n] tal que
    para cada i, 0 <= i <= n, crivo[i]  ́e True se i  ́e primo e
    crivo[i]  ́e False se i  ́e não  ́e primo.
    A lista crivo  ́e criada implementando o algoritmo do Crivo de Eratóstenes.
    Esta função retorna a lista crivo.

    """
    
    
    raizn = int(math.sqrt(n)) 
    
    crivo = [False, False]  
    for i in range(2, n+1, 1):
        crivo.append(True)

    for i in range(2, raizn+1, 1):
        if crivo[i]:
            for j in range(i*i, n+1, i):
                crivo[j] = False
                
    return crivo




#------------------------------------------------------------------------------
#--------------Definição da função criaListaPrimos(crivo) ---------------------
#------------------------------------------------------------------------------

def criaListaPrimos(crivo):
    """ (list) -> list
    Recebe uma lista crivo que foi criada utilizando o algoritmo do Crivo de 
    Eratóstenes. A partir da lista crivo, esta função cria e retorna uma lista
    chamada primos, contendo todos os números primos, em ordem crescente.
    """
    
    tamanho = len(crivo)
    primos = []
    
    for i in range(0, tamanho, 1):
        if crivo[i]:
            primos.append(i)  
     
    return primos



#------------------------------------------------------------------------------
#-------------Definição da função imprimeNumerosInteiros(a) -------------------
#------------------------------------------------------------------------------

def imprimeNumerosInteiros(a):
    
    """ 
    (list) -> NoneType
    Recebe uma lista a de n ́umeros inteiros e imprime todos os números da lista,
    escrevendo no máximo dez números em cada linha e de modo que fiquem
    ajustados nas colunas.
    """
    
    b = len(a) -1
    linhas = b // 10
    linhainc = b % 10

    for i in range(0, linhas):
        k = i * 10
        for j in range(k, k +10):
            print("%5d" %a[j], end = "")
        print("\n")
    
    if linhainc != 0 or b == 0:
        for i in range(linhas*10, b + 1):
            print("%5d" %a[i], end = "")
            
#------------------------------------------------------------------------------
#--------------Definição da maioriIntervaloSemPrimos(n)  ----------------------
#------------------------------------------------------------------------------
def maioriIntervaloSemPrimos(n):
    
    
    crivo = criaListaCrivoEratostenes(n)
    lista = criaListaPrimos(crivo)
    r = 0
    s = 0
    maiorintervalo = 0
    
    for i in range(0, len(lista)-1, 1):
        intervaloatual = lista[i + 1] - lista[i]
        
        if intervaloatual > maiorintervalo:
            maiorintervalo = intervaloatual
            r = lista[i]
            s = lista[i + 1]
    
    return r, s


#------------------------------------------------------------------------------
#-------------Definição da função imprimeNumerosInteiros(a) -------------------
#------------------------------------------------------------------------------
    
def testaConjecturaGoldbach(k):
    """ (int) -> list, bool
    Recebe um inteiro k > 2 e verifica se a Conjectura de Goldbach  ́e verdadeira
    para todo inteiro n par, 2 < n < k.Para isto, para cada tal inteiro n,
    esta função tenta encontrar dois números primos p e q tais que n = p + q.
    Se existir mais do que um tal par,escolha o par com o menor p 
    (e tal que p <= q).
    Obs.: Para alguns números pode existir mais de um par de primos.
    Por exemplo, 40 = 3 + 37 = 11 + 29 = 17 + 23.
    Neste caso, o par escolhido deve ser p, q, com p = 3 e q = 37.
    Para dar um certificado da validade da conjectura para os números pares n
    entre 2 e k, a função testaConjecturaGoldbach constrói uma lista chamada
    pares_primos que tem a seguinte propriedade:
    Como n  ́e par, n >= 4,  então n = 2 * i, onde i >= 2.
    Para cada i, i >= 2, pares_primos[i] armazena o primo p tal que n = p + q,
    onde p <= q  e  q = n - p  ́e primo. Apenas o valor de p  ́e armazenado j ́a
    que o valor de q  ́e precisamente n - p.
    A função testaConjecturaGoldbach retorna a lista pares_primos e retorna
    também True ou False dependendo se a conjectura for válida ou não para
    todo n par, 2 < n < k."""
    pares_primos = [0,0]
    
    crivo = criaListaCrivoEratostenes(k)
    lista = criaListaPrimos(crivo)    
    valeconj = True        
    q = 0
    i = 0
    p = 0
    
    for j in range(2, k//2 ,1):
        n = (2 * j)
        q = 0
        i = 0
        while i < len(crivo) - 2 and not crivo[q]:        
            p = lista[i]
            q = n - p
            
            if crivo[q]:
                pares_primos.append(p)
            
            i += 1
        
    
    if len(pares_primos) < k//2:
        valeconj = False
        
    return pares_primos, valeconj

#------------------------------------------------------------------------------
#---------------------Chama a função Principal---------------------------------
#------------------------------------------------------------------------------
main()
