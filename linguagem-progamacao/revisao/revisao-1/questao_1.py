'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 1
Feito por: Misla Wislaine

Enunciado:
Dado como entra um ponto p0 (p0x e p0y), um raio r e outro ponto p1 (p1x e p1y). Sendo p0 o centro do circulo e r o seu raio. Todos os valores são do tipo float. Verifique se o ponto p1 está dentro, fora ou na borda do circulo.
'''

def main():
    # Entrada do valores:
    entrada = list(map(float, input().split(",")))
    p0x, p0y, r, p1x, p1y = entrada
    
    # Coordenadas dos pontos
    p0 = (p0x, p0y)
    p1 = (p1x, p1y)

    # Cálculo da distância ao quadrado entre p0 e p1
    distancia_ao_quadrado = (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2
    raio_ao_quadrado = r ** 2

    if  distancia_ao_quadrado < raio_ao_quadrado:
        print('p1 está dentro do circulo')
    elif distancia_ao_quadrado == raio_ao_quadrado:
        print('p1 está na borda do circulo')
    else:
        print('p1 está fora do circulo')

if __name__ == "__main__":
    main()