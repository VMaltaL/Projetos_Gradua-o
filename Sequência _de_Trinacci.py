# -*- coding: utf-8 -*-
"""
Nome do aluno: Victoria M
     Disciplina: MAC0115  Introdução à Computação
     Exercício-Programa EP1A

        Definimos uma sequência de números inteiros, chamada sequência de Trinacci, da seguinte forma:

    T(0) = 0,   T(1) = 1,   T(2) = 1   e
    
    T(n) = T(n-3) + T(n-2) + T(n-1),  se n>=3.

  Os 15 primeiros números dessa sequência são:
    
    0    1    1    2   4    7   13   24   44   81   149   274   504   927   1705. 
  
         Este Ep foi feito apenas com conteúdo passado durante a aula ou 
    disponibilizado na página da disciplina do moodle.
"""

n = int(input("Insira o número inteiro maior ou igual a 0 para n:" ))


def main(n):
    print("Este programa calcula o T(n) de uma sequência de Trinacci, dado o n pelo usuário.")

    a = 0 #T(n-3) ou T(n)
    b = 1 #T(n-2) ou T(n+1)
    c = 1 #T(n-1) ou T(n+2)
    

    cont = 0 #contador


    while cont < n:
        d = a + b + c #calcula F(cont)
    
        #atualiza as variáveis 
        a = b
        b = c
        c = d
        cont = cont + 1
    
    print ("\nO T(",n,") da sequência de Trinacci é ", a, sep = "", end = ".\n")

#imprime somente o termo que estamos interessados, f(n).
"""
Usando cont = 0, estamos na verdade sempre interessados no F(a).
"""
main(n)