'''
Capítulo 1: Introdução à Programação das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

def main (): 
    nota_1 = float(input()) # Variável que recebe a primeira nota, ela está convertendo a string em um número ponto flutuante
    nota_2 = float(input()) # Variável que recebe a segunda nota, ela está convertendo a string em um número ponto flutuante
    nota_3 = float(input()) # Variável que recebe a terceira nota, ela está convertendo a string em um número ponto flutuante

    media = (nota_1 + nota_2 + nota_3)/3 # Variável que realiza a manipulação, fazendo o cálculo da média das notas e armazenando esse dado

    print(media) # Imprimindo a média das três notas

if __name__ == "__main__": 
    main() 
