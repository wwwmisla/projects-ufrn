# Capítulo 1

> **Capítulo 1: Introdução à programação em Python**
> 

## O que é programação de computadores?

É a arte e ciência de conceber e criar conjuntos de instruções que capacitam computadores a realizar tarefas específicas. 

- Lógica de Algoritmos → Linguagem de Programação;
- Mente Humana → Máquina.

Filosoficamente falando, programar é também uma forma de enxergar o mundo sob diferentes perspectivas, processos e abstrações.

Assim surge, Python, uma linguagem considerada de alto nível, sendo interpretada e multiparadigma. 

- Facilidade de Aprendizado e Uso.
- Versátil;
- Suporte a Vários Paradigmas de Programação.

Ela está presente em diversas áreas, sendo utilizada para simulação, análise e visualização de dados, desenvolvimento de aplicações web, dentre outras coisas.

## O que você precisa para começar?

1. **Computador com Acesso à Internet:**
    1. Facilita o download de pacotes adicionais ou até mesmo no acesso à documentação online, entretanto, é possível programar em Python em um ambiente offline.
2. **Editor de Texto ou IDE(Ambiente de Desenvolvimento Integrado):**
    1. [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/), [Visual Studio Code](https://code.visualstudio.com/), [Replit](https://replit.com/), [Google Colab](https://colab.research.google.com/), [Jupyter Notebook](https://jupyter.org/) e o [PyCharm](https://www.jetbrains.com/pycharm/).
3. **Interpretador Python:**
    1. Fazer o download do interpretador Python diretamente do site da Python Software Foundation (https://www.python.org/).

## Escrevendo seu primeiro programa em Python

Soma dois números e mostra o resultado. O arquivo pode ser chama de “soma.py” e o código é este:

```python
a = 1
b = 2
soma = a + b
print(soma)
```

Ao roda o programa, ele vai exibir:

```python
3
```

**Explicação do código:**

- **`a = 1`**: Define o valor 1 para a variável `a`.
- **`b = 2`**: Define o valor 2 para a variável `b`.
- **`soma = a + b`**: Soma os valores de `a` e `b` e guarda o resultado (3) na variável `soma`.
- **`print(soma)`**: Mostra o valor de `soma` na tela (3).

**O que são variáveis?**

Variáveis guardam dados para serem usados no programa. Aqui `a`,`b` e `soma` são variáveis.

**O que são funções?**

Funções realizam tarefas específicas. A função **`print`** mostra algo na tela.

**Como rodar o programa:**

1. Escreva o código em um editor de texto.
2. Salve como “soma.py”.
3. Abra o terminal ou prompt de comando.
4. Vá até a pasta onde o arquivo foi salvo.
5. Execute o código com o comando:

```python
   python soma.py
```

1. O resultado será o número 3, que é a soma de 1 e 2.

## Como um programa em Python funciona?

Desenvolvimento do Código Fonte → Salvo em arquivo com extensão “.py” → Enviado ao interpretador Python.

**Interpretador:** Vai ler e processar o código em Python, transforma em **bytecode**.

**PVM(Máquina Virtual Python):** Roda o programa, executando o bytecode, gerencia a memória e interage com o sistema operacional. 

Na versão **CPython**, por exemplo, o interpretador pode usar um **Compilador Just-In-Time (JIT)**, o que torna o desempenho do programa bem melhor.

![Funcionamento Interno do Python.](https://heltonmaia.com/pythonbook/_images/pythonWorks2.png)

**Figura: Funcionamento Interno do Python.**

## Estrutura básica de um programa em Python

A estrutura é simples, composta por um algoritmo (sequência de passos definidos para realizar uma tarefa) que envolve **entrada** (dados), **processamento** (etapas a serem seguidas) e **saída** (resultado).

Estrutura básica de um programa Python é:

```python
def main():
    # Bloco de código principal

if __name__ == "__main__":
    main()
```

- **`main()`**: A função principal do programa, chamada quando o código é executado.
- **Bloco de código principal**: É onde o programa faz seu trabalho, e o código é indentado para indicar que pertence ao bloco principal.
- **`if __name__ == "__main__":`**: Verifica se o arquivo está sendo executado diretamente como o programa principal. Se sim, a função `main()` é chamada.

**Exemplo de um programa simples:**

```python
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```

Para executar o programa, siga estes passos:

- Salve o código em um arquivo com extensão “.py” (por exemplo, “hello_world.py”).
- No terminal ou prompt de comando, execute o seguinte:

```python
python hello_world.py
```

<aside>
🚨

**Dica: A importância da indentação**

Em Python, a indentação não é apenas uma questão de estilo, mas uma parte essencial da sintaxe. Ela define a estrutura do programa e o agrupamento dos blocos de código. O uso de quatro espaços por nível de indentação é recomendado pela [**PEP 8**](https://peps.python.org/pep-0008/), o guia oficial de estilo do Python. Seguir essa recomendação não só melhora a legibilidade, como também mantém o código organizado e fácil de entender.

</aside>

## **Exemplo aprimorado: capturando nome e idade**

Aprendendo a interagir com o usuário. Neste exemplos, faremos um programa que solicita o nome e a idade do usuário, armazena essas informações e depois exibe na tela. Siga os passos abaixo:

- Crie um novo arquivo para o código;
- Insira o seguinte código no arquivo:

 

```python
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
print("Seu nome é:", nome)
print("Você tem", idade, "anos.")
```

`input` : Função que pede o nome e a idade do usuário;

`nome` `idade` : Variáveis que guardam as informações de entrada para que o programa consiga imprimi-las depois.

- Salve o arquivo e execute-o com o Python.
- Quando você rodar o programa, ele vai pedir o nome e a idade:
    
    ```python
    Qual é o seu nome? Ana Maria
    Qual é a sua idade? 25
    ```
    
- Após inserir as informações, o programa vai mostrar a saída:
    
    ```python
    Seu nome é: Ana Maria
    Você tem 25 anos.
    ```
    

Nesse exemplo, conseguimos fazer um programa interativo.

## **Comentando seu código**

Em Python, usamos o símbolo `#` para comentários de uma única linha, e `'''` ou `"""` para comentários que ocupam várias linhas.

- **Comentário de uma linha:**

```python
# Solicita o nome do usuário
nome = input("Qual é o seu nome? ")
```

- **Comentário de várias linhas com aspas simples:**

```python
'''
Este bloco de código solicita a idade do usuário
e armazena o valor na variável 'idade'.
'''
idade = input("Qual é a sua idade? ")
```

- **Comentário de várias linhas com aspas duplas:**

```python
"""
A seguir, exibimos o nome e a idade inseridos pelo usuário.
Esta parte do código é responsável pela exibição dos dados.
"""
print("Nome:", nome)
print("Idade:", idade)
```

- **Comentário explicando a lógica do código:**

```python
# Verifica se o usuário é maior de 18 anos para determinar a elegibilidade
elegivel = int(idade) > 18
```

**Dicas importantes:**

1. **Seja claro e objetivo;**
2. **Evite excessos;**
3. **Atualize seus comentários.**

## **Estratégias cientificamente fundamentadas para estudar programação**

### Repetição espaçada

A repetição espaçada é uma técnica de aprendizado que envolve revisar conceitos em intervalos crescentes, o que ajuda a fortalecer a retenção a longo prazo.

### Interleaving

Interleaving, ou a mistura de diferentes tópicos de estudo, é uma técnica que impede a sobrecarga de um único assunto, incentivando a aplicação flexível de vários conceitos.

### Prática ativa

A prática ativa envolve aprender programando de fato, ao invés de apenas ler ou assistir tutoriais passivamente.

### Compreensão profunda

Ao invés de apenas memorizar código ou comandos, busque uma compreensão mais profunda dos conceitos.

### Foco e mínima interrupção

A concentração contínua e sem distrações é crucial para o aprendizado eficaz, especialmente em campos como a programação, onde resolver problemas requer raciocínio lógico e atenção aos detalhes.

### Aprendizagem baseada em problemas

A abordagem de aprendizagem baseada em problemas (Problem-Based Learning) envolve focar em desafios práticos, ao invés de estudar conceitos isolados.

### Recursos diversificados

Combinar diferentes fontes de aprendizado é outra estratégia eficiente. Além de livros e artigos, explore tutoriais em vídeo, aulas interativas e cursos online.

### Espaço para reflexão

Refletir sobre o que você aprendeu, seja revisando mentalmente ou escrevendo em um diário, fortalece a retenção do conteúdo e permite identificar áreas que precisam de mais atenção.

### Revisão regular

O estudo contínuo e a revisão periódica dos tópicos ajudam a combater o esquecimento e a consolidar o conhecimento.

### Aprendizagem colaborativa

Participar de grupos de estudo ou discutir tópicos em fóruns online como o [Stack Overflow](https://stackoverflow.com/) promove o compartilhamento de ideias e oferece feedback valioso.

## **Exercícios**

1.  **Escreva um programa que imprime a famosa mensagem do mundo da programação.**

Neste exercício, você deve simplesmente exibir uma mensagem na tela. Não é necessário ler nenhuma entrada do usuário, apenas utilizar o comando print para exibir o texto desejado.

```python
# Teste 1
Saída: Olá Mundo!
```

1. **Neste exercício, você deve ler duas entradas: o nome de um aluno e sua matrícula. Em seguida, exiba uma mensagem de boas-vindas formatada com esses dados.**
```python
# Teste 1
Entrada:
Python da Silva
2024123456
Saída: Olá Python da Silva, Matrícula: 2024123456. Seja bem vindo!
```