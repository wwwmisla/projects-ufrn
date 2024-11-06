'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 7
Feito por: Misla Wislaine
'''

def main():
    id = int(input()) # Entrada do ID da ilha

    especie_1 = {1,2,3,4,5,6,7,8,9,10} # Ilhas preferidas pela Espécie 1
    especie_2 = {6,7,8,9,10,11,12,13,14,15,16,17} # Ilhas preferidas pela Espécie 2
    compartilhada = especie_1 & especie_2 # Interseção entre as ilhas preferidas

    if id in compartilhada:
        print(f"Ilha {id} é compartilhada entre espécie(s):1 2.")
    elif id in especie_1:
        print(f"Ilha {id} é exclusiva da Espécie 1.\nPortanto, não é compartilhada com outras espécies.")
    elif id in especie_2:
        print(f"Ilha {id} é exclusiva da Espécie 2.\nPortanto, não é compartilhada com outras espécies.")
    else:
        print(f"Ilha {id} não é preferida por nenhuma das espécies.")
        
if __name__ == "__main__":
    main()