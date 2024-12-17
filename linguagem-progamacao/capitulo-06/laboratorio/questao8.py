'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 8
Feito por: Misla Wislaine
'''

def gerar_prompt(titulo, descricao):
    """
    Gera um prompt formatado para modelos de IA.

    Args:
        titulo (str): O título do prompt.
        descricao (str): Uma breve descrição do contexto ou objetivo.

    Retorna:
        str: O prompt formatado.
    """
    prompt = f"=== TÍTULO ===\n{titulo}\n\nDescrição:\n{descricao}"
    
    return prompt

titulo, descricao = input().split(',', 1)
print(gerar_prompt(titulo.strip(), descricao.strip()))
