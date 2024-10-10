def main():
    # Cria um dicionário vazio para armazenar as informações do aluno
    aluno = {}

    # Coleta as informações do aluno
    aluno.__setitem__('nome', input())
    aluno.__setitem__('matricula', input())

    # Coleta as notas do aluno
    for i in range(1, 4):
        nota = float(input())
        aluno.__setitem__(f'nota_{i}', nota)  # Usando método especial para adicionar a nota

    # Calcula a média das notas usando os métodos especiais
    media = (aluno.__getitem__('nota_1') + aluno.__getitem__('nota_2') + aluno.__getitem__('nota_3')) / 3

    # Exibe os dados do aluno
    print(f"Nome: {aluno.__getitem__('nome')}")
    print(f"Matrícula: {aluno.__getitem__('matricula')}")
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
