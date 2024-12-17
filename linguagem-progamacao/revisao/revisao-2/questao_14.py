'''
Exercícios de Revisão de Linguagem de Programação - ECT3201
Criado por: Lucas de Oliveira Umbelino
Questão: 14
Feito por: Misla Wislaine

Enunciado:
(Questão do RespondeAi)

Escreva uma função “inva” em Python que recebe um dicionário d e retorna um dicionário “inverso” do dicionário dado, onde, a cada valor v de d está associada a lista das chaves de d que levam a v. Por exemplo:

dicio = {'a': 1,'b': 2,'c': 1,'d': 3,'e': 2}
dicio_saida = {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
'''

def inva(d):
    """
    Função para inverter um dicionário.
    Retorna um novo dicionário onde os valores originais tornam-se chaves,
    e as chaves originais tornam-se os valores (em listas).
    """
    
    # Criar um dicionário vazio para o dicionário inverso
    d_inverso = dict()
    
    # Percorrer as chaves e valores do dicionário original
    for chave, valor in d.items():
        # Se o valor ainda não está no dicionário inverso, cria uma nova lista
        if valor not in d_inverso:
            d_inverso[valor] = []
            
        # Adicionar a chave original à lista do valor no dicionário inverso
        d_inverso[valor].append(chave)
        
    # Retornar o dicionário inverso
    return d_inverso

def main():
    """
    Função principal para coletar o dicionário e inverter ele.
    """
    
    dicio = {}  # Cria um dicionário vazio para preencher dinamicamente
    
    print("Digite as chaves e valores para o dicionário. Digite 'sair' como chave para finalizar.")
    while True:
        chave = input("Digite o nome da chave (ou 'sair' para finalizar): ")
        if chave.lower() == 'sair':  # Finaliza a entrada se o usuário digitar 'sair'
            break
        
        valor = input(f"Digite o valor para a chave '{chave}': ")
        dicio[chave] = valor  # Adiciona a chave e valor ao dicionário
        
        # Inverte o dicionário
        dicio_invertido = inva(dicio)

        # Exibe o dicionário original
        print("\nDicionário original:")
        print(dicio)

        # Exibe o dicionário invertido
        print("\nDicionário invertido:")
        print(dicio_invertido)
        
if __name__ == "__main__":
    main()