'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada 
    frase_palavra = input()

    # Manipulando os valores
    comprimento = len(frase_palavra) # Comprimento da String usando a função len()
    primeira_letra = frase_palavra[0] # Primeira letra da String 
    ultima_letra = frase_palavra[-1] # Última letra da String
    invertida = frase_palavra[::-1] # Inverte a String
    
    # Saída 
    print(f"{comprimento}\n{primeira_letra}\n{ultima_letra}\n{invertida}")

if __name__ == "__main__": 
    main() 
