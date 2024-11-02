'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 1
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada - Receber 2 valores, um inteiro e um ponto flutuante
    n1 = int(input())
    n2 = float(input())

    # Manipulando os valores
    soma = n1 + n2 # Operação de soma
    subtracao = n1 - n2 # Operação de subtração
    multiplicacao = n1 * n2 # Operação de multiplicação
    divisao = n1 / n2 # Operação de divisão
    
    # Saída 
    print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}") # Utilizei f-string para ficar mais limpo o código

if __name__ == "__main__": 
    main() 
