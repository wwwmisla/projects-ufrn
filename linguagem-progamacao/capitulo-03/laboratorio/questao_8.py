'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 8
Feito por: Misla Wislaine
'''

def main():
    # Fase 1.
    # Lê toda a entrada do usuário em uma única linha e divide a string em uma lista usando espaços como delimitadores.
    entrada = input().split() 

    # Fase 2 & Fase 3.
    if entrada[0].lower() == "vermelha": # Verifica se a entrada é igual vermelha, nesse caso usamos o .lower() para que não haja erros ao verificar. 
        if entrada[1].lower() == "sim" and entrada[2].lower() == "sim" and entrada[3].lower() == "sim": # Verificamos se todas as entradas (menos a entrada[0]) são iguais a 'sim'(true|verdadeira), usamos o operador 'and' para saber se de fato todas as condições são verdadeiras, se uma condição for falsa, o resultado total é falso.
            print("Neo terá acesso a informações sobre a verdade.")
        if entrada[1].lower() == "não" or entrada[2].lower() == "não" or entrada[3].lower() == "não": # Verificamos se ao menos uma das entradas (menos a entrada[0]) são iguais a 'sim'(true|verdadeira), usamos o operador 'or' para saber disso, se ao menos uma condição for verdadeira, o resultado total é verdadeiro.
            print("A escolha é sua, Neo continua vivendo sua vida normal.")
    elif entrada[0].lower() == "azul": # Verifica se a entrada é igual a 'azul'.
        print("Neo continua vivendo sua vida normal.")
    else: # Se a entrada não foi igual a 'vermelha' e nem 'azul', então informa o erro de resposta inválida.
        print("Essa não é uma resposta válida, tente novamente.")
        
if __name__ == "__main__":
    main()