'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 11
Feito por: Misla Wislaine

Enunciado:
Faça uma função como entrada um valor inteiro N e retorne um valor inteiro.Está função deve calcular o valor do fatorial de N e retorna na função. O seu programa principal deve ter a entrada de um valor inteiro positivo e fazer a chamada da função.
'''

def fatorial(n):
    if n > 0: # Verifica se n é maior que 0
        fatorial = 1
        
        for i in range(1, n +1):
            fatorial *= i
            
        return print(f"O fatorial de {n} é {fatorial}.") # Retorna o valor do fatorial
    else:
        return print("O valor deve ser um número positivo") # Caso n não seja positivo

# Testando
n = int(input())
fatorial(n)