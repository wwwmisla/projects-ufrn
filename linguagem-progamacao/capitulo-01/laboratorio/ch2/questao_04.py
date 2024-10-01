def main():
    peso = float(input())
    altura = float(input())
    
    imc = peso/(altura*altura)
    
    if imc < 18.4:
        print(f"Seu IMC é {imc:.2f} (Abaixo do peso).")
    elif imc < 24.9:
        print(f"Seu IMC é {imc:.2f} (Saudável).")
    elif imc < 29.9:
        print(f"Seu IMC é {imc:.2f} (Sobrepeso).")
    elif imc < 34.9:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau I).")
    elif imc < 39.9:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau II).")
    else:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau III).")
        
if __name__ == "__main__":
    main()