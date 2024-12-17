'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 4
Feito por: Misla Wislaine
'''

import re

def validar_senha(senha):
    # Valida cada critério e retorna uma lista de booleanos
    comprimento_minimo = bool(re.search(r'.{8,}', senha))
    tem_letra_maiuscula = bool(re.search(r'[A-Z]', senha))
    tem_letra_minuscula = bool(re.search(r'[a-z]', senha))
    tem_numero = bool(re.search(r'\d', senha))
    
    return [comprimento_minimo, tem_letra_maiuscula, tem_letra_minuscula, tem_numero]

# Entrada do usuário
senha = input()

# Validação da senha
resultado = validar_senha(senha)

# Exibição dos resultados
print(f"Comprimento mínimo de 8 caracteres: {'OK' if resultado[0] else 'NÃO'}")
print(f"Pelo menos uma letra maiúscula: {'OK' if resultado[1] else 'NÃO'}")
print(f"Pelo menos uma letra minúscula: {'OK' if resultado[2] else 'NÃO'}")
print(f"Pelo menos um número: {'OK' if resultado[3] else 'NÃO'}")

# Mensagem final
if all(resultado):  # Verifica se todos os critérios foram atendidos
    print("Senha forte!")
else:
    print("Senha fraca!")
