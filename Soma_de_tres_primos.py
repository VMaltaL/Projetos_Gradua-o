# -*- coding: utf-8 -*-
"""
Nome do aluno: Victoria M
     Disciplina: MAC0115  Introdução à Computação
     Exercício-Programa EP1B

        Escreva um programa, na linguagem Python 3.x, que leia um número inteiro positivo n,
        e verifica se n é ou não a soma de três números primos consecutivos. 
        No caso de n ser tal soma, o seu programa deve imprimir também os números primos correspondentes.
  
         Este Ep foi feito apenas com conteúdo passado durante a aula ou 
    disponibilizado na página da disciplina do moodle.
"""

print("\nEsse programa calcula se um numero dado, n, é a soma de três números primos consecutivos.")


#------------------------------------------------------------------------------
#                           Função principal
#------------------------------------------------------------------------------


def main():
    
    n = int(input("Insira um número inteiro positivo para n: "))

    nat = 1
    soma = 0 #soma dos últimos primos
    p = 0 #penúltimo primo
    u = 0 #último primo
    a = 0 #atual
    
    while soma < n:
    
        if eh_primo(nat):
            p = u
            u = a
            a = nat
            
            soma = p + u + a
            
        nat += 1
            

    
    if soma == n and u != 0 and p != 0:
        print (".\nO número", n, "é a soma de três números primos consecutivos.") 
        print ("São eles: %d, %d e %d." %(p,u,a))
    
    else:
        print("O número", n, "não é a soma de três números primos consecutivos.")


#------------------------------------------------------------------------------
#                     função descobre se um número é primo
#------------------------------------------------------------------------------


def eh_primo(n):
    if n == 2:
        primo = True
        
    else: 
        if n == 1 or n % 2 == 0:
            primo = False
            
        else:
            
            nat = 3
            primo = True
            
            while nat * nat <= n and primo:
                
                if n % nat == 0:
                    
                    primo = False
                nat += 2
                
    return primo


#------------------------------------------------------------------------------
#                 Chama a função principal
#------------------------------------------------------------------------------
    

main()
