'''
Capítulo 5: Funções e Modularização das Listas de Linguagem de Programação - ECT3201
Questão: 9
Feito por: Misla Wislaine
'''

'''
Como resolver problemas recursivos?
- Entenda o problema: O que você quer calcular? Pode ser quebrado em subproblemas menores?
- Identifique o caso base: Quando a função deve parar de se chamar?
- Escreva o passo recursivo: Como dividir o problema em partes menores?
- Teste com exemplos simples: Use valores pequenos para ver como a função se comporta.
'''

def calcular_potencia(base, expoente):
    if expoente == 0:
        return 1
    if expoente < 0:
        return 1 / calcular_potencia(base, -expoente)
    return base * calcular_potencia(base, expoente -1)

base, expoente = map(int, input().split(",", 1))
print(f"{base}^{expoente} = {calcular_potencia(base, expoente)}")