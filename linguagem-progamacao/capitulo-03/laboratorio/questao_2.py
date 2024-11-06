'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def main():
    # Recebe o número 
    numero = int(input())

    # Verifica se o número é maior ou igual a 100 e menor ou igual a 1000.
    if 100 <= numero <= 1000:
        resto = numero % 5 # Calcula o resto da divisão do número por cinco.
        print(f"O resto da divisão de {numero} por 5 é {resto}.") # Imprime a saída
    else: 
        print("Por favor, insira um número inteiro positivo entre 100 e 1000.") # Imprime a saída
    
if __name__ == "__main__":
    main()