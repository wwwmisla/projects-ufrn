'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 17
Feito por: Misla Wislaine

Enunciado:
Considere um vetor de inteiros. Faça as seguintes funções:

A) Implemente uma função chamada ordenar_crescente que recebe um vetor como parâmetro e retorna uma versão ordenada em ordem crescente.

B) Crie uma função chamada ordenar_decrescente que recebe um vetor como parâmetro e retorna uma versão ordenada em ordem decrescente.

C) Crie uma função chamada ordenar_par_impar que recebe um vetor como parâmetro e retorna uma versão do vetor onde os elementos pares estão ordenados em ordem crescente e os ímpares ordenados em ordem decrescente.
'''

def ordenar_crescente(vetor):
    # Copia o vetor original para não modificar o original
    vetor_crescente = vetor[:]
    
    # Implementação do algoritmo de ordenação (Bubble Sort)
    n = len(vetor_crescente)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if vetor_crescente[j] > vetor_crescente[j + 1]:
                # Troca os elementos se estão fora de ordem
                vetor_crescente[j], vetor_crescente[j + 1] = vetor_crescente[j + 1], vetor_crescente[j]
    
    return vetor_crescente

def ordenar_decrescente(vetor):
    vetor_decrescente = vetor[:]
    
    # Implementação do algoritmo de ordenação (Bubble Sort) para ordem decrescente
    n = len(vetor_decrescente)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if vetor_decrescente[j] < vetor_decrescente[j + 1]:  # Comparação para decrescente
                vetor_decrescente[j], vetor_decrescente[j + 1] = vetor_decrescente[j + 1], vetor_decrescente[j]
    
    return vetor_decrescente

def ordenar_par_impar(vetor):
    # Separando os números pares e ímpares
    pares = [x for x in vetor if x % 2 == 0]  # Números pares
    impares = [x for x in vetor if x % 2 != 0]  # Números ímpares
    
    # Ordenando os pares em ordem crescente
    pares = ordenar_crescente(pares)
    
    # Ordenando os ímpares em ordem decrescente
    impares = ordenar_decrescente(impares)
    
    # Concatenando os pares e ímpares
    return pares + impares

def main():
    # Entrada: converte a string de entrada em uma lista de inteiros
    vetor = list(map(int, input("Digite os números separados por espaço: ").split()))
    
    # Exibindo o vetor original
    print(f"Vetor original: {vetor}")
    
    # Exibindo o vetor ordenado em ordem crescente
    print(f"Ordenado em ordem crescente: {ordenar_crescente(vetor)}")
    
    # Exibindo o vetor ordenado em ordem decrescente
    print(f"Ordenado em ordem decrescente: {ordenar_decrescente(vetor)}")
    
    # Exibindo o vetor com pares em ordem crescente e ímpares em ordem decrescente
    print(f"Ordenado pares em crescente e ímpares em decrescente: {ordenar_par_impar(vetor)}")

if __name__ == "__main__":
    main()
