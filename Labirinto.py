# -*- coding: utf-8 -*-
"""
Nome do aluno: Victoria M
     Disciplina: MAC0115  Introdução à Computação
     Exercício-Programa EP4

    Vamos representar um labirinto retangular atrav´es de uma matriz chamada labirinto, cujos elementos
s˜ao 0 ou −1, conforme a posi¸c˜ao correspondente do labirinto seja uma passagem livre ou uma parede, respectivamente. Dados dois pontos deste labirinto, chamados de origem e destino, desejamos saber se existe um
caminho entre a origem e o destino. Se existente, desejamos encontrar um caminho m´ınimo entre tais pontos.
Vamos impor que, a cada passo, seja permitido andar somente nas dire¸c˜oes horizontal ou vertical.
O prop´osito do exerc´ıcio-programa (EP4) ´e resolver o problema acima, conforme as instru¸c˜oes dadas a
seguir. Propomos dois procedimentos separados para encontrar (se existente) um caminho m´ınimo (mais curto
poss´ıvel) da origem para o destino. Primeiramente, vocˆe deve usar um algoritmo (explicado a seguir) para
marcar umas posi¸c˜oes da matriz. Depois, veremos como podemos usar essas marca¸c˜oes para encontrar (se
existente) um caminho m´ınimo.
  
         Este Ep foi feito apenas com conteúdo passado durante a aula ou 
    disponibilizado na página da disciplina do moodle.
"""

#------------------------------------------------------------------------------
#-------------------------FUNÇÃO PRINCIPAL-------------------------------------
#------------------------------------------------------------------------------

def main():
    """( )->NoneType
    
    Chama as funções le_cria_labirinto e marca_labirinto, usando na segunda
    os valores retornados pela primeira. Se existe um caminho, chama a função 
    determina_um_caminho com a matrizL. Chama as funções de impressão e imprime 
    numericamente e simbolicamente o labirinto e chama a função que imprime a 
    lista de posições do caminho.
    
    """
    print("\n\nEste programa lê um arquivo com uma matriz representando um "
          "labirinto e, se exite um caminho da origem ao destino, calcula "
          "o caminho mínimo.\n")
   
    
    

    labrinto = le_Cria_Labirinto()
    #salva as váriaveis com nomes mais claros
    matrizL = labrinto[0]
    lin_origem = labrinto[1]
    col_origem = labrinto[2]
    lin_destino = labrinto[3]
    col_destino = labrinto[4]
    
    
    marca_Labirinto(matrizL, lin_destino, col_destino)

    
    if matrizL[lin_origem][col_origem] > 0:
        caminho = determina_um_caminho(matrizL, lin_origem, col_origem)
        #salva as váriaveis com nomes mais claros
        matrizC = caminho[0]
        lista = caminho[1]
        
        print("\n")
        print(
"==============================================================================")
        print("\nImprime o labirinto numerado.", end = " ")
        imprime_labirinto_numericamente(matrizL)
        
        
        print(
"==============================================================================")
        imprime_labirinto_simbolicamente(matrizC)
        
        
        print(
"==============================================================================")

        imprime_caminho(lista)
    
    else:
        print("\nNão existe caminho da origem para o destino neste labirinto.\n")
        
    print(
"==============================================================================")

    

#------------------------------------------------------------------------------
#--------------FUNÇÃO le_Cria_Labririnto---------------------------------------
#------------------------------------------------------------------------------
    
    
def le_Cria_Labirinto():
    """
    () ->  matriz, int, int, int int
    Esta função lê todos os dados de um arquivo cujo nome deve ser fornecido
    pelo usuário (conforme descrito no item (a)). Ela cria uma matriz
    (com  moldura) com as informações lidas, e retorna essa matriz, os índices
    de linha e de coluna da posição da origem e os índices de linha e de coluna
    da posição do destino.
    """
    
    nomeArqEntrada = input("Digite o nome de um arquivo de entrada "
                           "(no formato txt) a ser lido: ")
     
    arqEntra = open(nomeArqEntrada, 'r')
    
    #ler informações da matriz
    linha = arqEntra.readline()
    lista = linha.split()
    m = int(lista[0]) #linha
    n = int(lista[1]) #coluna
    
    #lê origem
    linha = arqEntra.readline()
    lista = linha.split()
    lin_origem = int(lista[0]) 
    col_origem = int(lista[1]) 
    
    #lê destino
    linha = arqEntra.readline()
    lista = linha.split()
    lin_destino = int(lista[0]) 
    col_destino = int(lista[1])
    
    matriz = cria_Matriz(m + 1, n + 1 ,-1)
    linha = arqEntra.readline()
    lista = linha.split()
   
    for i in range(1, m +1, 1):
        for j in range(1, n +1, 1):
            matriz[i][j] = int(lista[j-1])
        linha = arqEntra.readline()
        lista = linha.split()
    
    

    return matriz, lin_origem, col_origem, lin_destino, col_destino
#------------------------------------------------------------------------------
#-----------------------FUNÇÃO cria_Matriz-------------------------------------
#------------------------------------------------------------------------------    
def cria_Matriz(m, n, valor):
    
    
    """(int, int, int) -> matriz
    
    Recebe o número de linhas, colunas e um inteiro, retorna uma matriz com
    moldura e preenchida com o valor em todas as posições
    """
    
    matriz= []
    
    for i in range(0, m + 1 ,1):
        linha = []
        for j in range(0, n + 1,1):
            linha.append(valor)
            
        matriz.append(linha)
           
    return matriz
    
#------------------------------------------------------------------------------
#-------------------------FUNÇÃO marca_Labirinto
#------------------------------------------------------------------------------    


def marca_Labirinto(matrizL, lin_destino, col_destino):
    """ (matriz, int, int) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, 
    representando um labirinto, e dois inteiros lin_destino e col_destino que
    são os índices de linha e de coluna da posição do destino nesse labirinto.
    Efetua a marcação da matrizL, conforme o algoritmo que foi descrito."""
    
    pares_linha_coluna = [(lin_destino, col_destino),]
    
    
    inicio = 0
    fim = len(pares_linha_coluna)
    
    k = 1
    matrizL[pares_linha_coluna[0][0]][pares_linha_coluna[0][1]] = k
    
    while inicio < fim:
        a = pares_linha_coluna[inicio]
        lin = a[0]
        col = a[1]
        
        k = matrizL[lin][col] + 1 
    
        if matrizL[lin + 1][col] == 0:
            pares_linha_coluna.append((lin + 1, col),)
            matrizL[lin + 1][col] = k 
            
            
        if matrizL[lin - 1][col] == 0:
            pares_linha_coluna.append((lin - 1, col),)
            matrizL[lin - 1][col] = k 
            
        if matrizL[lin][col + 1] == 0:
            pares_linha_coluna.append((lin, col + 1),)
            matrizL[lin][col + 1] = k 
            
        if matrizL[lin][col - 1] == 0:
            pares_linha_coluna.append((lin, col - 1),)
            matrizL[lin][col - 1] = k 
        
        
        inicio += 1
        fim = len(pares_linha_coluna)
   

#------------------------------------------------------------------------------
#-------------------FUNÇÃO determina_um_caminho--------------------------------
#------------------------------------------------------------------------------    

def determina_um_caminho(matrizL, lin_origem, col_origem):
    """ (matriz, int, int) -> matriz, list
    Recebe uma matriz de inteiros (com moldura) matrizL, representando um labirinto
    já marcado, e dois inteiros lin_origem e col_origem que são os índices de linha
    e de coluna da posição da origem nesse labirinto.
    A função supõe que existe um caminho da origem para o destino e determina um tal
    caminho de comprimento mínimo (utilizando, obrigatoriamente, o algoritmo descrito).
    [Ou seja, esta função só deve ser chamada quando se sabe que existe um tal caminho.]
    A função cria uma matriz de caracteres (como mostrada no exemplo), diferenciando
    as posições livres das posições que representam paredes, e indicando nessa matriz
    as posições da origem, do destino e do caminho encontrado.
    (Para facilitar, pode criar essa matriz com moldura.)
    Esta função cria também uma lista, onde cada elemento é um par representando
    os índices de linha e de coluna de uma posição do caminho encontrado.
    A função retorna a matriz e a lista criadas."""
    
    matrizC = cria_Matriz(len(matrizL) - 1, len(matrizL[0]) - 1, -1)
    
    for i in  range(0, len(matrizL), 1):
        for j in range(0, len(matrizL[0]),1):
            matrizC[i][j] = matrizL[i][j]

    
    
    k = matrizL[lin_origem][col_origem] -  1
    matrizC[lin_origem][col_origem] = "[O]"
    i = lin_origem
    j = col_origem
    lista = [(lin_origem, col_origem),]
    
    while k >= 1:
        if k != 1:
            if matrizC[i + 1][j] == k:
                matrizC[i + 1][j] = "[#]"
                lista.append((i + 1, j),)
                i += 1
            
            elif matrizC[i - 1][j] == k:
                matrizC[i - 1][j] = "[#]"
                lista.append((i - 1, j),)
                i -= 1
            
            elif matrizC[i][j + 1] == k:
                matrizC[i][j + 1] = "[#]"
                lista.append((i, j + 1),)
                j += 1
            
            elif matrizC[i][j - 1] == k:
                matrizC[i][j - 1] = "[#]"
                lista.append((i, j - 1),)
                j -= 1
       
        
        else:
            if matrizC[i + 1][j] == k:
                matrizC[i + 1][j] = "[D]"
                lista.append((i + 1, j),)
                i += 1
            
            elif matrizC[i - 1][j] == k:
                matrizC[i - 1][j] = "[D]"
                lista.append((i - 1, j),)
                i -= 1
            
            elif matrizC[i][j + 1] == k:
                matrizC[i][j + 1] = "[D]"
                lista.append((i, j + 1),)
                j += 1
            
            elif matrizC[i][j - 1] == k:
                matrizC[i][j - 1] = "[D]"
                lista.append((i, j - 1),)
                j -= 1            
            
        k -= 1
        
    for i in  range(0, len(matrizC), 1):
        for j in range(0, len(matrizC[0]),1):
            if type(matrizC[i][j]) != str:
                if matrizC[i][j] == -1: 
                   matrizC[i][j] = "---"
                else:
                    matrizC[i][j] = "[ ]"
                
    return matrizC, lista
   

#------------------------------------------------------------------------------
#-----------------FUNÇÃO imprime_labirinto_numericamente-----------------------   
#------------------------------------------------------------------------------

def imprime_labirinto_numericamente(matriz):
    """(matriz) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, representando
    um labirinto (antes ou depois da marcação).
    Imprime o labirinto (sem a moldura), no formato de matriz e ajustada
    nas colunas (exibindo também os índices das linhas e das colunas).
    """
    
    m = len(matriz)
    n = len(matriz[0])
    
    
    print("A primeira linha corresponde aos índices das colunas e a primeira\n"
          "coluna corresponde ao índices de linha. \n")
    print("O labirinto numericamente impresso:")
    for i in range(0, n - 1, 1):
        print("%6d" %(i), end = "")
        
    print("\n ")
    for i in range(1, m - 1,1):
        
        print ("%6d" %(i), end = "")
        
        for j in range(1, n - 1,1):
            print("%6d" %(matriz[i][j]), end = "")
        print("\n ") 
    
    
#------------------------------------------------------------------------------
#-------------------FUNÇÃO imprime_labirinto_simbolicamente--------------------
#------------------------------------------------------------------------------        
def imprime_labirinto_simbolicamente(matrizC):
    
    """(matriz)-> NoneType
    Recebe uma matriz de caracteres (com moldura) matrizC, representando
    um labirinto já com um caminho de comprimento mínimo.
    Imprime o labirinto (sem a moldura), no formato de matriz e ajustada
    nas colunas (exibindo também os índices das linhas e das colunas).
    """
    
    m = len(matrizC)
    n = len(matrizC[0])
      
    print("\nA primeira linha corresponde aos índices das colunas e a primeira\n"
          "coluna corresponde ao índices de linha. ")
    print("Significado de cada símbolo adotado:\n"
          "'[ ]' - Casa vazia\n"
          "'[#]' - Caminho achado\n"
          "'---' - Parede\n"
          "'[D]' - Destino\n"
          "'[O]' - Origem\n")
    print("O labirinto simbolicamente impresso:")

    for i in range(0, n - 1, 1):
        print("%5d" %(i), end = " ")
        
    print("\n ")
    for i in range(1, m - 1,1):
        
        print ("%5d" %(i), end = " ")
        
        for j in range(1, n - 1,1):
            print("%6s" %(matrizC[i][j]), end = "")
        print("\n ")     

#------------------------------------------------------------------------------
#-------------------FUNÇÃO imprime_caminho-------------------------------------
#------------------------------------------------------------------------------

def imprime_caminho(lin_col_caminho):
    """(list)-> NoneType
    
    Recebe uma lista lin_col_caminho, onde cada elemento é um par representando
    os índices de linha e de coluna de uma posição do caminho encontrado.
    Imprime os índices das posições do caminho encontrado (conforme o exemplo dado).
    """
    
    m = len(lin_col_caminho)

    
    print("\nLista de coordenadas do caminho mais curto achado: ")
    for i in range(0, m, 1):
        if i % 10 == 9:
            print(lin_col_caminho[i])  
            
        elif lin_col_caminho[i][1] >= 10:
            
            print(lin_col_caminho[i], end=' ')
        else: 
            print(lin_col_caminho[i], end='  ')
    print("\n\n")          
    

#------------------------------------------------------------------------------
#-----------------------CHAMA FUNÇÃO PRINCIPAL --------------------------------
#------------------------------------------------------------------------------    

main()
    
        