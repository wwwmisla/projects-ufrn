'''
Capítulo 1: Introdução à Programação das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def main (): 
    # Como estamos usando o sistema lop para resolver as questões da lista, não é necessário preencher o input com informação.
    nome = input() # Variável que recebe o nome do aluno
    matricula = int(input()) # Variável que recebe a matrícula do aluno e converte o input para um inteiro.

    print(f"Olá {nome}, Matrícula: {matricula}. Seja bem vindo!") # Para deixar a nossa saída com uma formatação mais limpa e legível, escolhi utilizar f-string que permite concatenar de uma forma mais completa através dos {} as variáveis que queremos concatenar na string.

if __name__ == "__main__": 
    main() 
