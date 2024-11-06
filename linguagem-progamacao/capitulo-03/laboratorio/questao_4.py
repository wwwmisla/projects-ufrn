'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

def main():
    # Solicita um número inteiro. 
    numero = int(input())

    # Verifica se ele está entre 10 e 20.
    if 10 <= numero <= 20:
        binario = bin(numero)[2::] # Converte o número em binário e tira o prefixo 0b.
        
        lista_bit = list(binario) # Cria uma lista e acrescenta dentro da lista os valores de binario
        
        print(lista_bit) # Imprime a lista
    else:
        print("O número inserido não está dentro do intervalo permitido.")

if __name__ == "__main__":
    main()