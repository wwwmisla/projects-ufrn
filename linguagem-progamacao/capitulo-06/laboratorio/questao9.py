'''
Capítulo 6: Manipulação de Strings das Listas de Linguagem de Programação - ECT3201
Questão: 9
Feito por: Misla Wislaine
'''

import re

def validar_campos(telefone, cpf):
    # Verifique se o telefone segue um dos formatos válidos especificados
    telefone_valido = re.search(r'\(\d{2}\)\s?\d{4,5}-\d{4}', telefone)
    
    # Verifique se o CPF segue o formato válido especificado
    cpf_valido = re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf)
    
    # Retorne uma string formatada indicando se cada campo é válido ou inválido
    resultado = f"Telefone válido: {'Sim' if telefone_valido else 'Não'}\nCPF válido: {'Sim' if cpf_valido else 'Não'}"
    
    return resultado

# Testando
telefone, cpf = input().split(',', 1)
print(validar_campos(telefone.strip(), cpf.strip()))
