def main():
    # Solicita a temperatura em celsius
    c = float(input())
    
    # Converte de Celsius para Fahrenheit
    f = (9/5) * c + 32
    
    # Saida formatada com duas casas decimais 
    print(f"A temperatura em Fahrenheit é: {f:.2f}")
    
if __name__ == "__main__":
    main()