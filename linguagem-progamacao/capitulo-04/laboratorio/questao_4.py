'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

def main():
    lista= list(map(float, input().split(','))) # Recebe uma lista de notas com números pontos flutuantes.
    soma_t, c_aprovado, c_reprovado = 0, 0, 0 # Cria os contadores. 

    for nota in lista: # Percorre a lista.
        if 0 <= nota <= 10: # Verifica se é um número entre 0 e 10.
            soma_t += nota # Soma o valor para depois ser usado na média.

            if nota >= 5: # Verifica se a nota é maior ou igual a cinco para ser aprovado.
                c_aprovado += 1
            else: # Verifica se a nota é menor que cinco para ser reprovado.
                c_reprovado += 1
        else: # Verifica se é uma nota inválida.
            print("Nota inválida.")
    
    media_t = (soma_t) / len(lista) # Calcula a média das notas.

    print(f"Número de Alunos Aprovados: {c_aprovado}\nNúmero de Alunos Reprovados: {c_reprovado}\nMédia da Turma: {media_t:.2f}") # Imprime as informações necessárias.

if __name__ == "__main__":
    main()