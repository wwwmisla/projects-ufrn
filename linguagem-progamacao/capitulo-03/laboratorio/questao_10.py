'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 10
Feito por: Misla Wislaine
'''

def main():
    # Recebe a entrada 
    altura_c, raio_c, altura_p, largura_p, comprimento_p = map(float, input().split())

    # Calcula os volumes
    volume_cone = (3.1416 * (raio_c ** 2) * altura_c) * 1/3

    volume_paralelepipedo = altura_p * largura_p * comprimento_p

    # Calcula as massas
    massa_c = volume_cone * 8
    massa_p = volume_paralelepipedo * 0.5

    # Compara os pesos
    if massa_p - massa_c < 5 and massa_p - massa_c > -5:
        print("O paralepípedo e o cone possuem o mesmo peso.")
    elif massa_c > massa_p:
        print(f"O cone é mais pesado com {massa_c:.2f}g.")
    elif massa_p > massa_c:
        print(f"O paralelepípedo é mais pesado com {massa_p:.2f}g.")
            
if __name__ == "__main__":
    main()