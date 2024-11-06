'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 10
Feito por: Misla Wislaine
'''

def main():
    # Solicitar ao usuário o valor de n
    n = int(input())

    # Inicializar a lista com os dois primeiros termos da sequência
    lista = [1, 1]

    # Calcular a sequência de Fibonacci até o n-ésimo termo
    for i in range(2, n):  # Começamos do índice 2, pois os dois primeiros termos já estão na lista
        proximo_elemento = lista[-1] + lista[-2]  # Soma dos dois últimos elementos
        lista.append(proximo_elemento)  # Adiciona o próximo elemento à lista

    # Exibir a sequência, limitando a lista ao número de termos desejados
    print(", ".join(map(str, lista[:n])))

if __name__ == "__main__":
    main()

