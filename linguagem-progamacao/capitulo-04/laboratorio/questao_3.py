'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 3
Feito por: Misla Wislaine
'''

import time # Importando o Módulo time.

def main():
    contagem = range(10,0,-1) # Preferi fazer a contagem fora para deixar o for mais limpo, usei o range para fazer a contagem range(inicio, fim, intervalo).

    for i in contagem: # Percorrendo cada número da contagem de 10 a 1
        if i != 1: # Verifica se o número do momento é diferente de 1 para inserir o espaço ao final.
            print(i, end=', ')
        else: # Nesse caso, o número sendo 1 ficará sem o espaço ao final.
            print(i)
        time.sleep(0.5) # Pausa a execução por 0.5 segundo após imprimir o número.

if __name__ == "__main__":
    main()