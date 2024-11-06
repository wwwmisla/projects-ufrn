'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 5
Feito por: Misla Wislaine
'''

def main():
    # Recebe lista de números inteiros.
    lista = list(map(int, input().split(',')))
    c = 0

    for i in lista:
        if 0 <= i < 15:
            fatorial = 1
            for j in range(1, i + 1):
                fatorial *= j 
            print(fatorial, end=' ')
        else:
            print("X", end=' ')
            c += 1
    
    print(f"\nQuantidade de números inválidos: {c}")
if __name__ == "__main__":
    main()