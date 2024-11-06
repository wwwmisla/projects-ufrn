'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 6
Feito por: Misla Wislaine

Enunciado:
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

def main():
    # Recebe um número inteiro positivo do usuário e o armazena na variável n.
    n = int(input())  
    
    # Inicializa uma lista vazia que será usada para armazenar os números da sequência de Fibonacci.
    lista = []
    
    # Um loop que itera de 0 até n-1 (ou seja, n iterações).
    for i in range(n):
        # Se o índice i for 0 ou 1, adiciona 1 à lista (os dois primeiros termos da sequência de Fibonacci).
        if i == 0 or i == 1:
            lista.append(1)
        else:
            # Para índices maiores que 1, calcula o próximo elemento da sequência como a soma dos dois elementos anteriores.
            proximo_elemento = lista[-1] + lista[-2]
            lista.append(proximo_elemento)  # Adiciona o próximo elemento calculado à lista.
    
    # Imprime a lista resultante que contém a sequência de Fibonacci até o n-ésimo termo.
    print(lista)

if __name__ == "__main__":
    main()