def main():
    # Entradas
    coordenadas = input().split()
    
    # Desenvolvimento
    x_min = int(coordenadas[0]) # Coordenadas do retangulo
    y_min = int(coordenadas[1]) # Coordenadas do retangulo
    x_max = int(coordenadas[2]) # Coordenadas do retangulo
    y_max = int(coordenadas[3]) # Coordenadas do retangulo
    
    x = int(coordenadas[4]) # Coordenadas do ponto
    y = int(coordenadas[5]) # Coordenadas do ponto
    
    # Manipulação das entradas 
    if (x_min < x < x_max) and (y_min < y < y_max):
        print("O ponto está dentro do retângulo.") # Saída
    elif (x_min <= x <= x_max) and (y_min <= y <= y_max):
        print("O ponto está tocando a borda do retângulo.") # Saída
    else:
        print("O ponto está fora do retângulo.") # Saída
    
if __name__ == "__main__":
    main()