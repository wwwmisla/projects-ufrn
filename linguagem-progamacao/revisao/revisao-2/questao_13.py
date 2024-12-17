'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 13
Feito por: Misla Wislaine

Enunciado:
Sem usar os operadores "/", "%" e "*".Crie uma função que receba o valor de dois números inteiros e retorne o resultado da divisão e o seu resto de divisão. Crie outra função que receba dois números inteiros e retorna a multiplicação.

OBS: Caso seja uma divisão invalida, retorne o valor -1. Exemplo: divisão por 0.
'''

def divisao_resto (dividendo, divisor):
    if divisor == 0: # Caso da divisão por 0
        return -1

    if dividendo < divisor:
        return (0, dividendo) # Base da recursão: quociente é 0 e o resto é o próprio dividendo
    else:
        quociente, resto = divisao_resto (dividendo - divisor, divisor)  # Subtração recursiva
        return (quociente + 1, resto) # Incrementa o quociente e retorna o resto
    
def multiplicacao(n1, n2):
    if n2 == 0: # Base da recursão: multiplicação por zero
        return 0
    if n2 < 0: # Tratar multiplicadores negativos
        return -multiplicacao(n1, -n2)
    return n1 + multiplicacao(n1, n2 - 1) # Soma recursiva

# Testando
n1, n2 = map(int, input().split(','))

resultado_div = divisao_resto(n1, n2)
if resultado_div == -1:
    print("Divisão inválida! Não é possível dividir por 0.")
else:
    quociente, resto = resultado_div
    print(f"Resultado da divisão: {quociente}, Resto: {resto}")

resultado_mult = multiplicacao(n1, n2)
print(f"Resultado da multiplicação: {resultado_mult}")