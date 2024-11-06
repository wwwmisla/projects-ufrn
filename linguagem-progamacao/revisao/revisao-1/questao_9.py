'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 9
Feito por: Misla Wislaine

Enunciado:
Faça um programa que dado um valor inteiro positivo N, sem usar a função bin, converta-o para um número binario.
'''

def main():
    n = int(input())  # Lê um número inteiro decimal do usuário e armazena em 'n'
    binario = ""      # Inicializa uma string vazia para armazenar o número binário

    # Executa o loop enquanto 'n' for maior que 0
    while n > 0:
        resto = n % 2             # Calcula o resto da divisão de 'n' por 2 (0 ou 1)
        binario = str(resto) + binario  # Adiciona o resto no início da string 'binario'
        n //= 2                   # Atualiza 'n' dividindo-o por 2 (inteira)

    # Converte o número binário de string para inteiro para remover possíveis zeros à esquerda
    binario = int(binario)

    # Imprime o número binário resultante
    print(binario)

if __name__ == "__main__":
    main()