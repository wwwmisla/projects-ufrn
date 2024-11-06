'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 9
Feito por: Misla Wislaine
'''

def main():
    # Recebe os valores dos catetos (adjacente e oposto) em uma única linha e os converte para float
    c_cateto_adjacente, c_cateto_oposto = map(float, input().split())

    # Calcula a hipotenusa usando o Teorema de Pitágoras: hipotenusa² = cateto_adjacente² + cateto_oposto²
    hipotenusa = (c_cateto_adjacente ** 2 + c_cateto_oposto ** 2) ** 0.5

    # Exibe o valor da hipotenusa formatado com duas casas decimais e a unidade "metros"
    print(f"{hipotenusa:.2f} metros") 
            
if __name__ == "__main__":
    main()