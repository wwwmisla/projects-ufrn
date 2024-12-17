'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 10
Feito por: Misla Wislaine
'''

def torre_de_hanoi(n, origem, auxiliar, destino):
    # Caso base: se há apenas 1 disco, mova diretamente
    if n == 1:
        print(f"Mover disco de{origem} para{destino}")
        return
    
    # Passo 1: Mover os n-1 discos do pino origem para o pino auxiliar
    torre_de_hanoi(n - 1, origem, destino, auxiliar)
    
    # Passo 2: Mover o disco maior (n) diretamente para o pino destino
    print(f"Mover disco de{origem} para{destino}")
    
    # Passo 3: Mover os n-1 discos do pino auxiliar para o pino destino
    torre_de_hanoi(n - 1, auxiliar, origem, destino)

# Testando 
n, origem, auxiliar, destino = input().split(",")
torre_de_hanoi(int(n), origem, auxiliar, destino)