'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 4
Feito por: Misla Wislaine

Enunciado:
Faça um programa que receba um número inteiro N e imprima todos os divisores de N.

Dica: Um divisor de N é um número que divide N sem deixar resto.
'''

def main():
    n = int(input())  # Recebe um inteiro positivo
    
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

if __name__ == "__main__":
    main()