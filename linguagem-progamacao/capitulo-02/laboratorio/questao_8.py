'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 8
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada | Recebendo cinco números inteiros distintos 
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    # Manipulando os valores 
    numeros = set() # Criando o conjunto numeros vazio

    # Adicionando os números ao conjunto
    numeros.add(n1)
    numeros.add(n2)
    numeros.add(n3)
    numeros.add(n4)
    numeros.add(n5)

    # Saída 
    print(numeros) # Imprime o conjunto completo

if __name__ == "__main__": 
    main() 
