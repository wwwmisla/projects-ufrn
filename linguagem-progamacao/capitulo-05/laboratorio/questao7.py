'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 7
Feito por: Misla Wislaine
'''

def soma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])

a = list(map(int, input().split(",")))
print(soma_recursiva(a))