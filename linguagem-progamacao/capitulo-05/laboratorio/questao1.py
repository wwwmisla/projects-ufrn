'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 1
Feito por: Misla Wislaine
'''

def ler_numeros(): 
    valores = input().split(",")
    
    numeros = []

    for valor in valores:
        if '.' in valor:
            numeros.append(float(valor))
        else:
            numeros.append(int(valor))
    
    num1 = numeros[0]
    num2 = numeros[1]
    num3 = numeros[2]
    
    return num1, num2, num3

def encontrar_maior_menor(num1, num2, num3):
    tupla = tuple()
    
    if num2 <= num1 and num1 >= num3:
        maior = num1
    elif num1 <= num2 and num2 >= num3:
        maior = num2
    elif num1 <= num3 and num3 >= num2:
        maior = num3
        
    if num2 >= num1 and num1 <= num3:
        menor = num1
    elif num1 >= num2 and num2 <= num3:
        menor = num2
    elif num1 >= num3 and num3 <= num2:
        menor = num3
        
    tupla = (maior, menor)
    
    return tupla

def main():
    num1, num2, num3 = ler_numeros()
    maior, menor = encontrar_maior_menor(num1, num2, num3)
    print(f"O menor número é: {menor}\nO maior número é: {maior}")

if __name__ == "__main__":
    main()