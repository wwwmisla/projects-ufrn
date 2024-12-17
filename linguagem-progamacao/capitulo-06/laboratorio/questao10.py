'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 10
Feito por: Misla Wislaine
'''

import requests
import re

def explorar_wiki(url, palavra_chave):
    """
    Busca o conteúdo de um artigo da Wikipedia e realiza manipulações com base em uma palavra-chave.

    Args:
        url (str): URL do artigo da Wikipedia.
        palavra_chave (str): Palavra-chave para buscas e análises no conteúdo do artigo.

    Retorna:
        dict: Um dicionário contendo o número de ocorrências da palavra-chave e o título do artigo.
    """
    
    # Remove aspas duplas (caso o usuário tenha incluído) e faz a requisição GET
    url = url.strip('"')  # Remove as aspas duplas da URL
    
    # Faz a requisição GET para o website
    response = requests.get(url)
    
    if response.status_code == 200:  
        # Obtém o conteúdo HTML da página
        conteudo = response.text
    
        # Extraia o título do artigo
        titulo = re.findall(r'<title>(.*?)</title>', conteudo)
        
        # Quantidade de vezes que a palavra_chave aparece no conteudo
        ocorrencias = len(re.findall(rf'\b{palavra_chave}\b', conteudo, re.IGNORECASE))
        
        # Organiza tudo em um dicionário
        resultado = {"titulo": titulo, "ocorrencias": ocorrencias}
        
        return resultado
    else:
        return {"erro": "Não foi possível acessar a url: {url}."}
    
# Testando 
url, palavra_chave = input().split(',', 1)
print(explorar_wiki(url.strip(), palavra_chave.strip()))