'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 5
Feito por: Misla Wislaine

Enunciado:
Escreva um programa em que receba um número inteiro N e crie uma lista contendo todos os números primos de 1 até N. Um número primo é um número maior que 1 que possui apenas dois divisores: 1 e ele mesmo. Por fim, imprima os valores da lista.
'''

def main():
    n = int(input())  # Recebe um inteiro positivo
    lista = list()
    
    for i in range(2, n + 1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            lista.append(i)
    print(lista)

if __name__ == "__main__":
    main()