'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

medalhas = input().split(',')
recorde_mundial = medalhas[-2]
primeira_medalha_pais = medalhas[-1]

def calcular_bonificacao (medalhas, recorde_mundial, primeira_medalha_pais):
    bonificacao = 0
    for medalha in medalhas:
        if medalha.lower() == "ouro":
            bonificacao += 50000
        elif medalha.lower() == "prata":
            bonificacao += 30000
        elif medalha.lower() == "bronze":
            bonificacao += 10000

    if recorde_mundial.lower() == "sim":
        bonificacao += 100000
      
    if primeira_medalha_pais.lower() == "sim":
        bonificacao += 50000

    return bonificacao

print(calcular_bonificacao(medalhas, recorde_mundial, primeira_medalha_pais))