'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 3
Feito por: Misla Wislaine

Enunciado:
Sem usar listas, dado um valor inteiro positivo chamado num:

Salve em num_invertido o valor invertido de num.
Com esté valor invertido, converta novamente para o valor original mas com os valores impares transformados em 0.
Com esté valor invertido, converta novamente para o valor original mas com os valores pares transformados em 0.
No fim, imprima esses valores.

Ex:

num = 123456
num_invertido = 654321
num_pares = 20406
num_impares = 103050
'''

def main():
    num = int(input())  # Recebe um inteiro positivo
    
    # Passo 1: Inverter o número
    aux = num
    num_invertido = 0
    while aux > 0:
        num_invertido = num_invertido * 10 + aux % 10  # Desloca dígitos e adiciona o último dígito de aux
        aux //= 10  # Remove o último dígito de aux

    # Passo 2: Criar o número com pares transformados em 0
    aux = num_invertido
    num_pares = 0
    multiplo = 1  # Para manter a posição correta ao construir num_pares
    while aux > 0:
        digito = aux % 10  # Pega o último dígito
        if digito % 2 == 0:  # Se for par
            num_pares += digito * multiplo  # Adiciona o dígito par na posição correta
        multiplo *= 10  # Atualiza a posição
        aux //= 10  # Remove o último dígito

    # Passo 3: Criar o número com ímpares transformados em 0
    aux = num_invertido
    num_impares = 0
    multiplo = 1  # Para manter a posição correta ao construir num_impares
    while aux > 0:
        digito = aux % 10  # Pega o último dígito
        if digito % 2 == 1:  # Se for ímpar
            num_impares += digito * multiplo  # Adiciona o dígito ímpar na posição correta
        multiplo *= 10  # Atualiza a posição
        aux //= 10  # Remove o último dígito

    # Impressão dos resultados
    print(num)
    print(num_invertido)
    print(num_pares)
    print(num_impares)

if __name__ == "__main__":
    main()