'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 5
Feito por: Misla Wislaine
'''

def main():
    # Entrada
    coordenadas = input().split()
    
    # Desenvolvimento | Criação das tuplas
    retangulo_inferior_esquerdo = (int(coordenadas[0]), int(coordenadas[1]))  # (x_min, y_min)
    retangulo_superior_direito = (int(coordenadas[2]), int(coordenadas[3]))   # (x_max, y_max)
    ponto = (int(coordenadas[4]), int(coordenadas[5]))                        # (x, y)

    # Extração das coordenadas das tuplas
    x_min, y_min = retangulo_inferior_esquerdo
    x_max, y_max = retangulo_superior_direito
    x, y = ponto
    
    # Manipulação das entradas 
    if (x_min < x < x_max) and (y_min < y < y_max):
        print("O ponto está dentro do retângulo.")
    elif (x == x_min or x == x_max) and (y_min <= y <= y_max) or (y == y_min or y == y_max) and (x_min <= x <= x_max):
        print("O ponto está tocando a borda do retângulo.")
    else:
        print("O ponto está fora do retângulo.")

if __name__ == "__main__":
    main()