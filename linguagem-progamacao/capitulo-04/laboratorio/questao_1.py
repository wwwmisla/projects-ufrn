'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 1
Feito por: Misla Wislaine
'''

def main():
    idades = map(int, input().split()) # Recebe as idades e transforma em inteiro 

    for idade in idades: # Laço de repetição for para percorrer cada idade da lista idades
        if idade < 13: # Verifica se é menor que 13
            print("Menor de idade") 
        elif 13 <= idade <= 17: # Verifica se está entre 13 e 17
            print("Adolescente")
        elif 18 <= idade <= 59: # Verifica se está entre 18 e 59
            print("Maior de idade") 
        else: # Verifica se está entre 60 ou mais
            print("Idoso")
        
if __name__ == "__main__":
    main()