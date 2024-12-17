'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 6
Feito por: Misla Wislaine
'''

def contar_pares_impares(numeros): # Função p/ contar
    pares, impares = 0, 0
    
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

def contar_positivos_negativos(numeros):
    positivos, negativos = 0, 0
    
    for numero in numeros:
        if numero >= 0:
            positivos += 1
        else: 
            negativos += 1
            
    return positivos, negativos
    
lista_numeros = list(map(int, input().split(',')))
pares, impares = contar_pares_impares(lista_numeros)
positivos, negativos = contar_positivos_negativos(lista_numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
