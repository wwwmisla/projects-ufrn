'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 3
Feito por: Misla Wislaine
'''

def main():
    # Solicita a temperatura em Celsius
    t_celsius = float(input())

    # Manipulando os valores
    t_fahrenheit = ((9/5) * t_celsius) + 32 # Converte de Celsius para Fahrenheit

    # Imprimindo o resultado | Saída formatada com duas casas decimais
    print(f"A temperatura em Fahrenheit é: {t_fahrenheit:.2f}")
    
if __name__ == "__main__":
    main()