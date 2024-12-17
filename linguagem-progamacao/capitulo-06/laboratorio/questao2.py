'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 2
Feito por: Misla Wislaine
'''

def criar_moldora(texto, caractere):
    # Comprimento total da moldura
    largura = len(texto) + 4
    
    # Linha superior e inferior
    linha_decorativa = caractere * largura
    
    # Linha do texto centralizada
    linha_texto = f"{caractere} {texto} {caractere}"
    
    # Junção da moldura
    moldura = f"{linha_decorativa}\n{linha_texto}\n{linha_decorativa}"
    
    return moldura

# Testando
texto, caractere = input().split(",", 1)
moldura = criar_moldora(texto, caractere)
print(moldura)