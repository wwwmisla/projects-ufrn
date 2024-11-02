'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 11
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada | Recebendo os números
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())
    numero4 = int(input())
    numero5 = int(input())

    # Manipulando os valores 
    lista = [numero1, numero2, numero3, numero4, numero5] # Cria a lista e preenche com os valores

    # Avalia se cada número é par ou ímpar
    resultado1 = "par" if lista[0] % 2 == 0 else "ímpar"
    resultado2 = "par" if lista[1] % 2 == 0 else "ímpar"
    resultado3 = "par" if lista[2] % 2 == 0 else "ímpar"
    resultado4 = "par" if lista[3] % 2 == 0 else "ímpar"
    resultado5 = "par" if lista[4] % 2 == 0 else "ímpar"

    # Saída | Imprime os resultados
    print(f"O número {lista[0]} é {resultado1}.")
    print(f"O número {lista[1]} é {resultado2}.")
    print(f"O número {lista[2]} é {resultado3}.")
    print(f"O número {lista[3]} é {resultado4}.")
    print(f"O número {lista[4]} é {resultado5}.")

if __name__ == "__main__": 
    main() 
