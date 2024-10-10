def main():
    # Solicita ao usuário que insira duas strings
    string1 = input()
    string2 = input()

    # Transforma a primeira string em maiúsculas
    string1_maiusculas = string1.upper()

    # Transforma a segunda string em minúsculas
    string2_minusculas = string2.lower()

    # Concatena as duas strings
    string_concatenada = string1_maiusculas + " " + string2_minusculas

    # Imprime os resultados
    print(f"{string1_maiusculas}")
    print(f"{string2_minusculas}")
    print(f"{string_concatenada}")

if __name__ == "__main__":
    main()
