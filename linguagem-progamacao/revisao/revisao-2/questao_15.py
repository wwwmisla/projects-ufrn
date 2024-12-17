'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 15
Feito por: Misla Wislaine

Enunciado:
Escreva uma função chamada contar_frases que recebe um texto como entrada e retorna um dicionário. Nesse dicionário, as chaves devem ser as frases do texto e os valores devem ser a quantidade de vezes que cada frase aparece. Considere que uma frase termina quando há um ponto (.), exclamação (!), interrogação (?), virgula (,) ou espaço ( ).
'''

import re

def contar_frases(texto): 
    """
    Função para contar a frequência de frases em um texto.
    Uma frase é considerada qualquer sequência de texto separada por ., !, ?, , ou espaço.
    """
    
    dicionario = dict() # Cria dicionário vazio
    
    # Usando regex para dividir o texto nas frases mencionadas
    frases = re.split(r'[.!?, ]+', texto)
    
    # Removendo frases vazias causadas por múltiplos separadores consecutivos
    frases = [frase for frase in frases if frase]
    
    # Implementa as chaves e os valores ao dicionário
    for frase in frases:
        if frase in dicionario:
            dicionario[frase] += 1
        else:
            dicionario[frase] = 1
            
    return dicionario 

def main():
    texto = input("Digite o texto:\n") # Recebe texto
    
    resultado = contar_frases(texto) # Chama a função 'contar_frases' e passa o argumento 'texto' salvando na variável chamada 'resultado'
    
    print("Contagem de frases:")
    
    for frase, ocorrencias in resultado.items():
        print(f"'{frase}': {ocorrencias}")

if __name__ == "__main__":
    main()