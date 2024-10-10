def main():
    # Solicita o peso e altura do usuário
    peso = float(input())
    altura = float(input())
    
    # Calcula o IMC
    imc = peso/(altura ** 2)
    
    # Classifica o IMC de acordo com a tabela
    if imc < 18.4:
        categoria = "Abaixo do peso"
    elif imc < 24.9:
        categoria = "Saudável"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    elif imc < 34.9:
        categoria = "Obesidade grau I"
    elif imc < 39.9:
        categoria = "Obesidade grau II"
    else:
        categoria = "Obesidade grau III"
        
    # Exibe o resultado
    print(f"Seu IMC é {imc:.2f} ({categoria}).")
        
if __name__ == "__main__":
    main()