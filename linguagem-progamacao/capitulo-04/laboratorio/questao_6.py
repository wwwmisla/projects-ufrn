'''
Capítulo 4: Controle de Fluxo e Números Aleatórios das Listas de Linguagem de Programação - ECT3201
Questão: 6
Feito por: Misla Wislaine
'''

'''
Como resolver essa questão:
- (1) Gerar o número secreto; 
- (2) Loop de 20 tentativas; 
- (3) Entrada do Jogador e Validação do Palpite; 
- (4) Palpite Único do Computador e Validação do Palpite; 
- (5) Verificar acertos; 
- (6) Dicas; 
- (7) Números de tentativas esgotado. 
- (8) Extra -> Histórico de palpites. 
'''

import random

def main():
    numero_aleatorio = random.randint(1, 100)  # Gerar número aleatório entre 1 e 100
    cont_tentativas = 0  # Contador de tentativas
    # random.seed(100)  # Definir a semente para reprodutibilidade
    # print(f"(Dica para teste: o número aleatório é {numero_aleatorio})")

    # Intervalo para o palpite do jogador e do computador com base nas dicas
    intervalo_jogador = [1, 100]
    intervalo_computador = [1, 100]
    palpites_computador = set()  # Armazena os palpites do computador para evitar repetição

    for tentativas in range(20, 0, -1):  # Limite de 20 tentativas
        palpite_jogador = int(input())
        
        # Gera um palpite único para o computador
        while True:
            palpite_computador = random.randint(intervalo_computador[0], intervalo_computador[1])
            if palpite_computador not in palpites_computador:
                palpites_computador.add(palpite_computador)
                break

        # print(f"Palpite do computador: {palpite_computador}")

        cont_tentativas += 1

        # Verificar se houve um acerto (computador, jogador ou ambos)
        if palpite_jogador == numero_aleatorio and palpite_computador == numero_aleatorio:
            print(f"Empate! Ambos adivinharam o número. Foram {cont_tentativas} tentativas, parabéns!")
            break
        elif palpite_jogador == numero_aleatorio:
            print(f"Jogador venceu! Foram {cont_tentativas} tentativas, parabéns!")
            break
        elif palpite_computador == numero_aleatorio:
            print(f"O computador venceu! Foram {cont_tentativas} tentativas, parabéns!")
            break

        # Se não acertaram, fornecer dicas e ajustar intervalos
        if palpite_jogador != numero_aleatorio:
            if palpite_jogador > numero_aleatorio:
                print(f"Dica para o jogador: o número é menor do que {palpite_jogador}!")
                intervalo_jogador[1] = palpite_jogador - 1
            else:
                print(f"Dica para o jogador: o número é maior {palpite_jogador}!")
                intervalo_jogador[0] = palpite_jogador + 1

        if palpite_computador != numero_aleatorio:
            if palpite_computador > numero_aleatorio:
                print(f"Dica para o computador: o número é menor {palpite_computador}!")
                intervalo_computador[1] = palpite_computador - 1
            else:
                print(f"Dica para o computador: o número é maior {palpite_computador}!")
                intervalo_computador[0] = palpite_computador + 1

        # Verificar se esgotaram as tentativas
        if tentativas == 1:
            print(f"Você perdeu, pois esgotou as tentativas! O número era {numero_aleatorio}.")
            break

        print(f"Tentativas restantes: {tentativas - 1}")

if __name__ == "__main__":
    main()