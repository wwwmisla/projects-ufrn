'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 5
Feito por: Misla Wislaine
'''

import re

def limpar_dados_sensor(dados):
    # Remove caracteres especiais
    dados = re.sub(r'[@#$&^]', '', dados)
    # Remove espaços extras
    dados = re.sub(r'\s+', ' ', dados)
    
    return dados.strip()

# Entrada do usuário
dados = input()
# Saída do processamento
print(limpar_dados_sensor(dados))