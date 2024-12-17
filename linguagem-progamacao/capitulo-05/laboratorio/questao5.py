'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 5
Feito por: Misla Wislaine
'''

def leitura_dados():
    a, b, c = map(float, input().split(','))
    
    return a, b, c
    
def possivel_calcular(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    
    if a == 0:
        return False # Não é possível calcular (a = 0)
    
    if discriminante < 0:
        return False # Não é possível calcular (discriminante  < 0)
        
    return True  # É possível calcular

def calcular_raizes(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante > 0:
        raiz1 = (-b + (discriminante ** 0.5)) / (2 * a) # Raiz positiva
        raiz2 = (-b - (discriminante ** 0.5)) / (2 * a) # Raiz negativa
        print(f'R1 = {raiz1:.2f}')
        print(f'R2 = {raiz2:.2f}')

# Programa principal
a, b, c = leitura_dados()

if possivel_calcular(a, b, c):  # Verifica se é possível calcular
    calcular_raizes(a, b, c)
else:
    print("Impossível calcular")