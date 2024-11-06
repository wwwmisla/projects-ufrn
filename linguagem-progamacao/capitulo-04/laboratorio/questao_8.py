'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 8
Feito por: Misla Wislaine
'''

def main():
    lista_leitura = list(map(int,input().split(","))) # Ler numero
    lista_repeticao = list()
    
    # Verificar se é primo 
    for numero in lista_leitura:
        if numero > 1:
            primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                lista_repeticao.append(numero)

    # Imprimir nova lista
    print(", ".join(map(str, lista_repeticao)))
    
if __name__ == "__main__":
    main()