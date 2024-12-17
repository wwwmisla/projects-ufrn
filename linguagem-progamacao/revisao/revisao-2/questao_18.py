'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 18
Feito por: Misla Wislaine

Enunciado:
Faça uma função recursiva que receba uma frase e uma letra, e retorne quantas vezes a letra aparece na frase.
'''

def contar_letra(frase, letra):
    # Caso base: se a frase estiver vazia, retorna 0
    if not frase:
        return 0
    
    # Verifica se o primeiro caractere é a letra desejada
    if frase[0] == letra:
        # Se for, conta 1 e chama recursivamente para o restante da frase
        return 1 + contar_letra(frase[1:], letra)
    
    # Se não for, apenas chama recursivamente para o restante da frase
    return contar_letra(frase[1:], letra)

# Entrada do usuário separada por vírgula
entrada = input().split(',', 1) # Divide a entrada em duas partes no máximo (frase e letra)
# Limpa os espaços e formata a entrada
frase = entrada[0].strip() # Remove espaços em excesso da frase
letra = entrada[1].strip().lower() # Remove espaços e converte a letra para minúscula
# Chama a função para contar as ocorrências da letra
resultado = contar_letra(frase.lower(), letra) # Coloca a frase em minúsculas para garantir que não haja problemas de case
# Imprime o resultado final formatado
print(f"A letra '{letra}' aparece {resultado} vezes na frase: '{frase}'.")