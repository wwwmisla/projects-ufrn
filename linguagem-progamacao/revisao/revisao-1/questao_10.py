'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 10
Feito por: Misla Wislaine

Enunciado:
Dado um número inteiro positivo N, mostre o fatorial N.
'''

def main():
    # Lê um número inteiro positivo do usuário
    n = int(input("Digite um número inteiro positivo: "))

    # Inicializa a variável fatorial como 1 (fatorial de 0 é 1)
    fatorial = 1

    # Calcula o fatorial multiplicando números de 1 até N
    for i in range(1, n + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"O fatorial de {n} é {fatorial}.")

if __name__ == "__main__":
    main()