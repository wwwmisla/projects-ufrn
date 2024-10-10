def main():
    # Solicita ao usuário que insira 5 números
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())
    numero4 = int(input())
    numero5 = int(input())

    # Cria uma lista com os números fornecidos
    lista = [numero1, numero2, numero3, numero4, numero5]

    # Avalia se cada número é par ou ímpar
    resultado1 = "par" if lista[0] % 2 == 0 else "ímpar"
    resultado2 = "par" if lista[1] % 2 == 0 else "ímpar"
    resultado3 = "par" if lista[2] % 2 == 0 else "ímpar"
    resultado4 = "par" if lista[3] % 2 == 0 else "ímpar"
    resultado5 = "par" if lista[4] % 2 == 0 else "ímpar"

    # Imprime os resultados
    print(f"O número {lista[0]} é {resultado1}.")
    print(f"O número {lista[1]} é {resultado2}.")
    print(f"O número {lista[2]} é {resultado3}.")
    print(f"O número {lista[3]} é {resultado4}.")
    print(f"O número {lista[4]} é {resultado5}.")

if __name__ == "__main__":
    main()
