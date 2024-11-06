'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 2
Feito por: Misla Wislaine

Enunciado:
Dado como entra um ponto p0 (p0x e p0y), dois raios r1 e r2, e outro ponto p1 (p1x e p1y). Sendo p0 o centro do circulo e r1 e r2 os seus raios. Verifique em qual area o ponto p1 vai estar.

Obs: Leve em consideração de que o usuario sempre vai colocar r1 sendo menor do que r2.
'''

def main():
    # Entrada do valores:
    entrada = list(map(float, input().split(",")))
    p0x, p0y, r1, r2, p1x, p1y = entrada
    
    # Coordenadas dos pontos
    p0 = (p0x, p0y)
    p1 = (p1x, p1y)

    # Cálculo da distância ao quadrado entre p0 e p1
    distancia_ao_quadrado = (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2
    r1_ao_quadrado = r1 ** 2
    r2_ao_quadrado = r2 ** 2

    if  distancia_ao_quadrado < r1_ao_quadrado:
        print('p1 está na area 1')
    elif distancia_ao_quadrado == r1_ao_quadrado:
        print("p1 está na borda da area 1 e area 2")
    elif r1_ao_quadrado < distancia_ao_quadrado < r2_ao_quadrado:
        print("p1 está na area 2")
    elif distancia_ao_quadrado == r2_ao_quadrado:
        print("p1 está na borda da area 2 e area 3")
    else:
        print("p1 está na area 3")

if __name__ == "__main__":
    main()