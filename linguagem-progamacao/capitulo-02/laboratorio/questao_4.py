'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada 
    peso = float(input())
    altura = float(input())

    # Manipulando os valores
    imc = peso / (altura ** 2)

    # Classifica o IMC de acordo com a tabela
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25.0:
        classificacao = "Saudável"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        classificacao = "Obesidade grau I"
    elif 35.0 <= imc < 40.0:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    '''
    Outra forma de classificar
    Em cada elif, só precisamos especificar o limite superior, pois sabemos que as faixas anteriores já foram excluídas.
    Esse formato simplifica o código, mantendo-o legível e sem redundância, pois cada elif depende implicitamente do fato de que o imc já foi filtrado pelas condições anteriores.
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25.0:
        classificacao = "Saudável"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
    elif imc < 35.0:
        classificacao = "Obesidade grau I"
    elif imc < 40.0:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    '''
    
    # Saída | Exibe o resultado
    print(f"Seu IMC é {imc:.2f} ({classificacao}).")

if __name__ == "__main__": 
    main() 
