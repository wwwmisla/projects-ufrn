def main():
    numeros = set()  # Cria um conjunto vazio

    # Solicita ao usuário cinco números inteiros distintos
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())
    numero4 = int(input())
    numero5 = int(input())

    # Adiciona os números ao conjunto
    numeros.add(numero1)
    numeros.add(numero2)
    numeros.add(numero3)
    numeros.add(numero4)
    numeros.add(numero5)

    print(f"{numeros}")  # Imprime o conjunto completo

if __name__ == "__main__":
    main()
