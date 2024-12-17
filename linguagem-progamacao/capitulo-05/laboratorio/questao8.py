'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 8
Feito por: Misla Wislaine
'''

# Função Fibonacci
def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero -1) + fibonacci(numero - 2)

# Função Soma
def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])
    
# Saída
entrada = input() # Recebe entrada

lista_numeros = list(map(int, entrada.split(","))) # Lista de números 

# Faz o calculo para cada numero
resultados_fibonacci = [fibonacci(numero) for numero in lista_numeros] 

# Calculo da soma total 
soma = soma(resultados_fibonacci)

# Saída final
print(soma)