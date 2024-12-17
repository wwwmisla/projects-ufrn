'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 3
Feito por: Misla Wislaine
'''

def busca_palavras_chave(texto, palavras_chave):
    texto_convertido = texto.lower()  # Converte o texto para minúsculas
    resultado = dict()  # Dicionário para armazenar as palavras-chave e suas contagens

    for palavra in palavras_chave:  # Percorre a lista de palavras-chave
        palavra = palavra.strip()  # Remove espaços extras ao redor da palavra-chave
        # Conta as ocorrências da palavra no texto
        contador = texto_convertido.count(palavra.lower()) # Pegamos o texto e usamos a função .count()
        resultado.update({palavra: contador})  # Adiciona ao dicionário a contagem da palavra
    
    return resultado  # Retorna o dicionário com as contagens

# Leitura de entrada
entrada = input().split(",", 1)  # Divide a entrada em duas partes: texto e palavras-chave
texto = entrada[0].strip()  # O texto é a primeira parte
palavras_chave = entrada[1].split(",")  # A segunda parte são as palavras-chave, que serão convertidas em lista

# Chama a função e imprime o resultado
print(busca_palavras_chave(texto, palavras_chave))
