'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 7
Feito por: Misla Wislaine
'''

def main():
    entrada = input().split(',')

    if entrada[0].lower() == "tipo1":
        for numero in range(1,(int(entrada[1]) + 1)):
            print("*" * numero)
    elif entrada[0].lower() == "tipo2":
        for numero in range(int(entrada[1]), 0, -1):
            print("*" * numero)
    else:
        print("Entrada inválida.")
        
if __name__ == "__main__":
    main()