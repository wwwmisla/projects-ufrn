'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 6
Feito por: Misla Wislaine
'''

# Entrada 
nome_experimento, valores, valor_esperado = input().split(",") # Divide a entrada
valores_medidos = list(map(float, valores.strip().split())) # Separa por espaço
valor_esperado = float(valor_esperado) # Converte em float

# Desenvolvimento -> Cálculo média e diferença absoluta
def gerar_relatorio(nome_experimento, valores_medidos, valor_esperado):
    # Calculo média valores medidos 
    media = sum(valores_medidos) / len(valores_medidos)

    # Calculo diferença absoluta
    diferenca_absoluta = abs(media - valor_esperado)

    relatorio = f"Experimento: {nome_experimento}\nMédia dos valores medidos: {media:.2f}\nDiferença em relação ao valor esperado: {diferenca_absoluta:.2f}"

    return print(relatorio)

# Saída
gerar_relatorio(nome_experimento, valores_medidos, valor_esperado)