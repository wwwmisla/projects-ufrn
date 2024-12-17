'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 12
Feito por: Misla Wislaine

Enunciado:
Faça uma função recursiva como entrada um valor inteiro N e retorne um valor inteiro.Está função deve calcular o valor do fatorial de N e retorna na função. O seu programa principal deve ter a entrada de um valor inteiro positivo e fazer a chamada da função.

OBS: Obrigatorio do uso da recursividade
'''

def fatorial(n):
    if n == 1:
        return 1
    
    return n * fatorial(n - 1)

n = int(input())
print(fatorial(n))