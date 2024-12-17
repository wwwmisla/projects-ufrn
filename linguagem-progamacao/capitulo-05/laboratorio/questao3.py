'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 3
Feito por: Misla Wislaine
'''

import math

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

def area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area

def calcular_area():
    #print("Escolha a área que deseja calcular:")
    #print("1. Triângulo")
    #print("2. Círculo")
    #print("3. Retângulo")
    #print("4. Sair do programa")
    
    opcao = int(input())
    
    if opcao == 1:
        base = float(input())
        altura = float(input())
        area = area_triangulo(base, altura)
        print(f'A área do triângulo é: {area:.2f}')
    elif opcao == 2:
        raio = float(input())
        area = area_circulo(raio)
        print(f'A área do círculo é: {area:.2f}')
    elif opcao == 3:
        comprimento = float(input())
        largura = float(input())
        area = area_retangulo(comprimento, largura)
        print(f'A área do retângulo é: {area:.2f}')
    elif opcao == 4:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")

calcular_area()