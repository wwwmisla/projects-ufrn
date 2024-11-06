'''
Capítulo 3: Operadores e Expressões das Listas de Linguagem de Programação - ECT3201
Questão: 6
Feito por: Misla Wislaine
'''

def main():
    # Recebe todas as entradas
    login = input().split()

    # Cria o dicionário com todas informações
    usuarios_senhas = {
        login[0]: login[1],
        login[2]: login[3],
        login[4]: login[5]
    }

    # Verifica as credenciais conforme os dados do dicionário
    if login[6] in usuarios_senhas and usuarios_senhas[login[6]] == login[7]:
        print(f"Login bem-sucedido! Bem-vindo, {login[6]}.")
    else:
        print("Acesso negado. Credenciais inválidas.")
if __name__ == "__main__":
    main()