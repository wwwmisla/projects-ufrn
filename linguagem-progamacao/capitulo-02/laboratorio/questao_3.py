'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 3
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada 
    string_1 = input().lower() # Recebe o valor da primeira String e utiliza a função lower para deixar a String em minúscula 
    string_2 = input().lower() # Recebe o valor da segunda String e utiliza a função lower para deixar a String em minúscula 

    # Manipulando os valores
    if string_1 == string_2: # Verifica se a string_1 é igual a string_2 
        print("São iguais") # Saída 
    else:
        print("São diferentes") # Saída 

if __name__ == "__main__": 
    main() 
