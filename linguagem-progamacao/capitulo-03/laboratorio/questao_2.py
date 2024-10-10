def main():
    # Numero inteiro positivo 
    numero = int(input())
    
    if 100 <= numero <= 1000:
        resto = numero % 5     # Resto da divisao por 5
        print(f"O resto da divisão de {numero} por 5 é {resto}.")     # Saida positivo
    else:
        print("Por favor, insira um número inteiro positivo entre 100 e 1000.")     # Saida erro
    
if __name__ == "__main__":
    main()