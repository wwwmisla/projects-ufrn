'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 9
Feito por: Misla Wislaine
'''

import random

def main():
    # Receber a semente do usuário
    semente = int(input())
    random.seed(semente)  # Definir a semente para geração de números aleatórios

    # Gerar a combinação vencedora
    combinacao_vencedora = set(random.sample(range(1, 51), 5))  # 5 números únicos entre 1 e 50
    #print("Combinação vencedora:", combinacao_vencedora)  # Exibir a combinação vencedora (opcional)

    # Contar o número de jogos realizados
    contador_jogos = 0

    # Loop para simular os jogos até que um ganhador seja encontrado
    while True:
        contador_jogos += 1  # Incrementar o contador de jogos
        jogo_atual = set(random.sample(range(1, 51), 5))  # Gerar um novo jogo de 5 números únicos

        # Verificar se o jogo atual corresponde à combinação vencedora
        if jogo_atual == combinacao_vencedora:
            #print("Combinação vencedora if:", combinacao_vencedora)  # Exibir a combinação vencedora (opcional)
            break  # Se for um ganhador, sair do loop

    # Exibir o número total de jogos necessários
    print(f"Número de jogos necessários: {contador_jogos}")

if __name__ == "__main__":
    main()
