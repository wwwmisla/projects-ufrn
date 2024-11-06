'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 8
Feito por: Misla Wislaine

Enunciado:
(Questão do RespondeAi)

Faça um programa que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ seja informado, após o fim da leitura, imprima o nome do aluno que possui a maior nota. Obs.: Use dicionário para resolver essa questão.
'''

def main():
    # Cria um dicionário vazio para armazenar os nomes dos alunos e suas notas.
    alunos = {}

    while True:
        # Lê o nome do aluno.
        nome = input("Digite o nome do aluno (ou 'oooo' para finalizar): ")
        
        # Verifica se o nome é 'oooo' para encerrar a entrada de dados.
        if nome == 'oooo':
            break
        
        # Lê a nota do aluno e converte para float.
        nota = float(input(f"Digite a nota de {nome}: "))
        
        # Armazena o nome e a nota no dicionário.
        alunos[nome] = nota

    # Verifica se há alunos no dicionário antes de encontrar o maior.
    if alunos:
        # Inicializa as variáveis para o aluno com a maior nota.
        aluno_maior_nota = None
        maior_nota = -float('inf')  # Menor valor possível para começar a comparação
        
        # Itera sobre o dicionário para encontrar o aluno com a maior nota.
        for nome, nota in alunos.items():
            if nota > maior_nota:
                maior_nota = nota
                aluno_maior_nota = nome
        
        # Exibe o aluno com a maior nota.
        print(f"O aluno com a maior nota é {aluno_maior_nota}, com nota {maior_nota}.")
    else:
        print("Nenhum aluno foi registrado.")

if __name__ == "__main__":
    main()