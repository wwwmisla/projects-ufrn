'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 16
Feito por: Misla Wislaine

Enunciado:
Sem usar a função bin. Faça uma função recursiva que receba um valor N e retorne o valor de N em binario.
'''

def decimal_binario(n):
    """
    Função recursiva para converter um número decimal para binário.
    """
    
    # Caso base: Se n for 0, retornamos uma string vazia
    if n == 0:
        return ''
    # Calcula o resto da divisão por 2 (0 ou 1)
    resto = n % 2
    # Faz a chamada recursiva com n // 2 e adiciona o resto ao fina
    return decimal_binario(n // 2) + str(resto)

def main():
    n = int(input('Digite um número decimal:\n')) # Lê um número inteiro do usuário
    if n == 0: # Caso especial para n = 0
        print(f"Valor Decimal: {n}\nValor Binário: 0")
    else:
        binario = decimal_binario(n) # Chama a função recursiva
        print(f"Valor Decimal: {n}\nValor Binário: {binario}") # Imprime o número binário resultante
        
if __name__ == "__main__":
    main()
