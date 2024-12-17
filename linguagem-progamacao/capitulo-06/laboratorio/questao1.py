'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 1
Feito por: Misla Wislaine
'''

def manipular_string(entrada):
    elemento_um = entrada[0]  # Primeiro caractere
    elemento_ultimo = entrada[-1]  # Último caractere
    tres_primeiros = entrada[0:3]  # Três primeiros caracteres
    tres_ultimos = entrada[-3:]  # Três últimos caracteres
    inverte_ordem = entrada[::-1]  # String invertida

    # Remove vogais
    remove_vogais = ""  # String vazia para armazenar resultado
    for letra in entrada:
        if letra.lower() not in 'aeiou':  # Checa se não é vogal
            remove_vogais += letra  # Adiciona somente as consoantes

    # Se todas as letras forem vogais, retorna a entrada original
    if remove_vogais == "":
        remove_vogais = entrada

    lista = [
        elemento_um, elemento_ultimo, tres_primeiros,
        tres_ultimos, inverte_ordem, remove_vogais
    ]
    return lista

entrada = input()
print(manipular_string(entrada))