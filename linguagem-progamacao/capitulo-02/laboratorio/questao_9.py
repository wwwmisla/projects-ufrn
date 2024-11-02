'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 9
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada | Recebendo três diferentes números inteiros para os conjuntos 'a' e 'b'.
    n1_a = int(input())
    n2_a = int(input())
    n3_a = int(input())
    n1_b = int(input())
    n2_b = int(input())
    n3_b = int(input())

    # Manipulando os valores 
    conjunto_a = set() # Cria o conjunto 'a' vazio
    conjunto_b = set() # Cria o conjunto 'b' vazio

    # Adicionando os números aos conjuntos com o método .add()
    conjunto_a.add(n1_a) # Adiciona n1_a ao conjunto 'a'
    conjunto_a.add(n2_a) # Adiciona n2_a ao conjunto 'a'
    conjunto_a.add(n3_a) # Adiciona n3_a ao conjunto 'a'

    conjunto_b.add(n1_b) # Adiciona n1_b ao conjunto 'b'
    conjunto_b.add(n2_b) # Adiciona n2_b ao conjunto 'b'
    conjunto_b.add(n3_b) # Adiciona n3_b ao conjunto 'b'    

    # Realizando as operações 
    conjunto_uniao = conjunto_a | conjunto_b # Realiza a união do conjunto 'a' com conjunto 'b' através do |
    conjunto_intersecao = conjunto_a & conjunto_b # Realiza a interseção do conjunto 'a' com conjunto 'b' através do &
    conjunto_diferenca = conjunto_a - conjunto_b # Realiza a diferença do conjunto 'a' com conjunto 'b' através do -

    # Saída 
    print(f"União: {conjunto_uniao}\nInterseção: {conjunto_intersecao}\nDiferença: {conjunto_diferenca}")

if __name__ == "__main__": 
    main() 
