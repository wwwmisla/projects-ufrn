'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def main():
    l_palavras = input().split() # Recebe uma lista de palavras

    for palavra in l_palavras: # Percorre a lista de palavras
        if palavra == palavra[::-1]: # Verifica se é um palíndromo
            print("Sim", end=' ')
        else: # Verifica se não é um palíndromo
            print("Não", end=' ')

if __name__ == "__main__":
    main()