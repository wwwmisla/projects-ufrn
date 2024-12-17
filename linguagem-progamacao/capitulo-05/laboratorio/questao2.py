'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def ler_dados():
    peso, altura = map(float, input().split(","))

    return peso, altura

def calcula_imc(peso, altura):
    imc = peso / (altura * altura)

    return imc

def classificar_imc(imc):
    classificacao = "";
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif imc <= 39.9:
        classificacao = "Obesidade grau 2"
    elif imc >= 40:
        classificacao = "Obesidade grau 3"

    return classificacao

peso, altura = ler_dados()
imc = calcula_imc(peso, altura)
classificacao = classificar_imc(imc)
print(f'Seu IMC é {imc:.2f} - Classificação: {classificacao}')