'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 7
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada 
    contato = {"nome": input(), "telefone": input(), "endereco": input()} # Cria o dicionário contato com as chaves nome, telefone e endereco, em paralelo insere os valores das chaves os quais são recebidos por meio do input.

    # Manipulando os valores | Saída 
    print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Endereço: {contato['endereco']}.") # Aqui estamos imprimindo os valores de nome, telefone e endereco os quais temos acesso através dos valores coletados no dicionário contato. 

    '''
    Outra forma de fazer:
    contato = {} -> Cria um dicionário vazio

    contato["nome"] = input() -> Cria a chave nome e coleta o valor nome do input

    nome = contato["nome"] -> Acessando os valores coletados

    print(f"Nome: {nome}") -> Imprimindo
    '''

if __name__ == "__main__": 
    main() 
