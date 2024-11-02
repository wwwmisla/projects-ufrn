'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 5
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada | Recebendo as cincos frutas, como não podemos usar o laço de repetição recebi uma de cada vez, mas poderia ter usado a função split, por exemplo
    fruta_1 = input()
    fruta_2 = input()
    fruta_3 = input()
    fruta_4 = input()
    fruta_5 = input()

    # Manipulando os valores
    frutas = [fruta_1, fruta_2, fruta_3, fruta_4, fruta_5] # Cria a lista e preenche ela com as frutas

    # Saída 
    print(f"Lista de frutas: {frutas}")
    
if __name__ == "__main__": 
    main() 
