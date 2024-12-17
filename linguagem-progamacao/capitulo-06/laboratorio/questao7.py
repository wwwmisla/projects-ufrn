'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 7
Feito por: Misla Wislaine
'''

import re

def analisar_frase(frase, palavra_alvo):
    # Remove espaços extras da palavra-alvo
    palavra_alvo = palavra_alvo.strip()
    # Define o padrão para buscar a palavra-alvo, considerando apenas palavras inteiras
    padrao = fr"\b{palavra_alvo}\b"
    
    # Encontra todas as ocorrências da palavra na frase
    todas_ocorrencias = re.findall(padrao, frase)
    quantidade = len(todas_ocorrencias) # Conta quantas vezes a palavra aparece
    
    if quantidade > 0:
        # Obtém a posição da primeira ocorrência da palavra
        primeira_ocorrencia = re.search(padrao, frase).start()
        # Exibe os resultados
        print(f'A palavra "{palavra_alvo}" está presente: Sim')
        print(f'Número de ocorrências: {quantidade}')
        print(f'Posição da primeira ocorrência: {primeira_ocorrencia}')
    else:
        # Indica que a palavra não foi encontrada
        print(f'A palavra "{palavra_alvo}" está presente: Não')
        print(f'Número de ocorrências: 0')
        print(f'Posição da primeira ocorrência: -1')
        
# Recebe a entrada do usuário no formato "frase, palavra_alvo"
frase, palavra_alvo = input().split(',', 1)
analisar_frase(frase, palavra_alvo)