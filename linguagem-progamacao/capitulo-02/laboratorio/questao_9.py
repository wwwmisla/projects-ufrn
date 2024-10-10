def main():
    # Inicializa os conjuntos
    conjunto_a = set()
    conjunto_b = set()

    # Solicita ao usuário que insira três números inteiros para o conjunto A
    for i in range(3):
        numero = int(input())
        conjunto_a.add(numero)

    # Solicita ao usuário que insira três números inteiros para o conjunto B
    for i in range(3):
        numero = int(input())
        conjunto_b.add(numero)

    # Realiza as operações
    uniao = conjunto_a | conjunto_b # Ou conjunto_a.union(conjunto_b)
    intersecao = conjunto_a & conjunto_b # Ou conjunto_a.intersection(conjunto_b)
    diferenca = conjunto_a - conjunto_b # Ou conjunto_a.difference(conjunto_b)

    # Imprime os resultados
    print(f"União: {uniao}")
    print(f"Interseção: {intersecao}")
    print(f"Diferença: {diferenca}")

if __name__ == "__main__":
    main()
