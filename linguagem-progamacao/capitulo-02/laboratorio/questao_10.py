'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 10
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada | Recebendo duas Strings 
    string_1 = input()
    string_2 = input()

    # Manipulando os valores 
    string_maiuscula = string_1.upper() # Transformando a string_1 em maiúscula 
    string_minuscula = string_2.lower() # Transformando a string_2 em minúscula

    string_concatenada = string_maiuscula + " " + string_minuscula # Concatenando a string_maiuscula com a string_minuscula

    # Saída 
    print(f"{string_maiuscula}\n{string_minuscula}\n{string_concatenada}")

if __name__ == "__main__": 
    main() 
