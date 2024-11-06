'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 7
Feito por: Misla Wislaine

Enunciado:
Faça um programa que leia cinco conjuntos de dois valores, onde o primeiro valor representa o número do aluno e o segundo valor representa a sua altura em centímetros. Armazene esses dados em um dicionário, onde a chave é o número do aluno e o valor é a altura.

Em seguida, encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas respectivas alturas.
'''

def main():
    # Cria um dicionário vazio para armazenar os dados dos alunos.
    # A chave será o número do aluno e o valor será a altura do aluno.
    alunos = {}

    # Loop para receber os dados de 5 alunos.
    for i in range(5):
        numero_aluno = int(input("Digite o número do aluno: "))  # Recebe o número do aluno.
        altura_aluno = int(input("Digite a altura do aluno em cm: "))  # Recebe a altura do aluno.
        alunos[numero_aluno] = altura_aluno  # Armazena o número e altura do aluno no dicionário.

        # Para o primeiro aluno, inicializa as variáveis de maior e menor altura.
        if i == 0:
            maior_altura = altura_aluno  # Define a altura do primeiro aluno como a maior altura inicial.
            aluno_mais_alto = numero_aluno  # Define o primeiro aluno como o aluno mais alto inicialmente.
            menor_altura = altura_aluno  # Define a altura do primeiro aluno como a menor altura inicial.
            aluno_mais_baixo = numero_aluno  # Define o primeiro aluno como o aluno mais baixo inicialmente.

    # Segundo loop para verificar o aluno mais alto e o mais baixo.
    # A função items() permite iterar sobre os pares (número do aluno, altura) no dicionário.
    for numero_aluno, altura_aluno in alunos.items():
        # Verifica se a altura do aluno atual é maior que a maior altura registrada.
        if altura_aluno > maior_altura:
            maior_altura = altura_aluno  # Atualiza a maior altura.
            aluno_mais_alto = numero_aluno  # Atualiza o número do aluno mais alto.
        # Verifica se a altura do aluno atual é menor que a menor altura registrada.
        if altura_aluno < menor_altura:
            menor_altura = altura_aluno  # Atualiza a menor altura.
            aluno_mais_baixo = numero_aluno  # Atualiza o número do aluno mais baixo.

    # Exibe o resultado com o número e a altura do aluno mais alto e do aluno mais baixo.
    print(f"Aluno mais alto: {aluno_mais_alto}, Altura: {maior_altura} cm")
    print(f"Aluno mais baixo: {aluno_mais_baixo}, Altura: {menor_altura} cm")


if __name__ == "__main__":
    main()