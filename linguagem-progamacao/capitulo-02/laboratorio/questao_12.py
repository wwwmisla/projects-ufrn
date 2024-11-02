'''
Capítulo 2: Tipos de dados e Estruturas Condicionais das Listas de Linguagem de Programação - ECT3201
Questão: 12
Feito por: Misla Wislaine
'''

def main (): 
    # Entrada 
    aluno = dict()

    # Manipulando os valores 

    # Coletando informações do aluno
    aluno.update({"nome": input()}) # Coleta o nome do aluno
    aluno.update({"matricula": input()}) # Coleta a matrícula do aluno
    aluno.update({"nota1": float(input())}) # Coleta a nota1 do aluno
    aluno.update({"nota2": float(input())}) # Coleta a nota2 do aluno
    aluno.update({"nota3": float(input())}) # Coleta a nota3 do aluno

    # Calculando a média do aluno
    media = (aluno.get("nota1") + aluno.get("nota2") + aluno.get("nota3")) / 3
    
    # Saída 
    print(f"Nome: {aluno.get('nome')}\nMatrícula: {aluno.get('matricula')}\nMédia: {media:.2f}")
if __name__ == "__main__": 
    main() 
