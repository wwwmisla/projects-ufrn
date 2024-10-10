def main():
    lista_frutas = []  # Cria uma lista vazia para armazenar as frutas

    # Solicita 5 frutas
    for i in range(5):  # Loop para solicitar 5 frutas
        fruta = input()  # Solicita a fruta
        lista_frutas.append(fruta)  # Adiciona a fruta à lista

    print(f"Lista de frutas: {lista_frutas}")  # Imprime a lista completa

if __name__ == "__main__":
    main()
