# Integrantes: Davi Pimentel, Giuseppe Parrini, Mateus Alves, Pedro Miclos
#
# Projeto Final - Fundamentos de Computação e Algoritmos de Programação
# Tema: Quiz Interativo sobre Lógica de Programação com Python
#
# Observação sobre bibliotecas: o único módulo importado é o "random", que é um módulo NATIVO do Python (não é uma biblioteca externa/terceira, como numpy ou pandas, e não precisa ser instalado com pip). Ele é necessário para sortear, a cada execução, 10 perguntas diferentes dentro do banco de 25 perguntas. Os módulos "time" e "os" mencionados na proposta NÃO são utilizados em nenhum momento neste código.
import random

# Banco de perguntas armazenado como uma LISTA DE DICIONÁRIOS. Cada pergunta é um dicionário e, dentro dele, a chave "alternativas" guarda uma LISTA com as 4 opções (índice 0 = A, índice 1 = B, índice 2 = C, índice 3 = D). Ou seja, temos uma lista (banco) que contém dicionários, e cada dicionário contém outra lista (alternativas) -> estrutura equivalente a uma matriz de dados.

# Perguntas são organizadas por temas, para que o feedback final possa indicar quais assuntos precisam de revisão. O tema de cada pergunta é armazenado na chave "tema" do dicionário.
BANCO_PERGUNTAS = [
    # Variáves
    {"pergunta": "Qual é a forma correta de criar uma variável chamada idade com o valor 25 em Python?",
     "alternativas": ["idade = 25", "int idade = 25", "declare idade = 25", "idade := 25"],
     "correta": "A", "tema": "Variáveis"},

    {"pergunta": 'Qual é o tipo de dado da variável x após a linha: x = "10"?',
     "alternativas": ["int", "float", "str", "bool"],
     "correta": "C", "tema": "Variáveis"},

    {"pergunta": "Após executar: a = 5  seguido de  a = a + 1, qual é o valor final de a?",
     "alternativas": ["Erro de sintaxe", "6", "5", "Duas variáveis são criadas"],
     "correta": "B", "tema": "Variáveis"},

    {"pergunta": "Qual função do Python é usada para verificar o tipo de uma variável?",
     "alternativas": ["typeof()", "type()", "class()", "kind()"],
     "correta": "B", "tema": "Variáveis"},

    {"pergunta": "Qual das opções abaixo é um nome de variável válido em Python?",
     "alternativas": ["1nome", "nome-completo", "nome_completo", "nome completo"],
     "correta": "C", "tema": "Variáveis"},

    # Estruturas Condicionais
    {"pergunta": "Qual estrutura é usada para tomar decisões com base em uma condição em Python?",
     "alternativas": ["for", "while", "if", "def"],
     "correta": "C", "tema": "Estruturas Condicionais"},

    {"pergunta": 'O que o código abaixo imprime?\n  x = 7\n  if x % 2 == 0:\n      print("Par")\n  else:\n      print("Impar")',
     "alternativas": ["Par", "Impar", "Erro", "Nada e impresso"],
     "correta": "B", "tema": "Estruturas Condicionais"},

    {"pergunta": "Qual operador é usado para verificar se dois valores são iguais em Python?",
     "alternativas": ["=", "==", "===", "!="],
     "correta": "B", "tema": "Estruturas Condicionais"},

    {"pergunta": "Em um if/elif/else, quando o bloco elif é executado?",
     "alternativas": ["Sempre, independente do if",
                       "Quando a condicao do if e falsa e a do elif e verdadeira",
                       "Apenas quando if e else falham",
                       "Nunca, se houver else"],
     "correta": "B", "tema": "Estruturas Condicionais"},

    {"pergunta": "Qual é o resultado da expressão: (5 > 3) and (2 > 4)?",
     "alternativas": ["True", "False", "Erro de sintaxe", "None"],
     "correta": "B", "tema": "Estruturas Condicionais"},

    # Estrurturas de repetição
    {"pergunta": "Qual laço é mais indicado quando sabemos exatamente quantas vezes repetir, como ao percorrer uma lista?",
     "alternativas": ["while", "for", "if", "def"],
     "correta": "B", "tema": "Estruturas de Repetição"},

    {"pergunta": "O que o código abaixo imprime?\n  contador = 0\n  while contador < 3:\n      print(contador)\n      contador += 1",
     "alternativas": ["0 1 2", "1 2 3", "0 1 2 3", "Loop infinito"],
     "correta": "A", "tema": "Estruturas de Repetição"},

    {"pergunta": "Qual a principal diferença entre for e while em Python?",
     "alternativas": ["for sempre repete infinitamente",
                       "while serve so para listas",
                       "for percorre uma sequencia conhecida; while repete enquanto uma condicao for verdadeira",
                       "Nao ha diferenca"],
     "correta": "C", "tema": "Estruturas de Repetição"},

    {"pergunta": "O que pode causar um laço while infinito?",
     "alternativas": ["Usar range() corretamente",
                       "A condicao do while nunca se tornar falsa",
                       "Usar for em vez de while",
                       "Declarar a variavel antes do laco"],
     "correta": "B", "tema": "Estruturas de Repetição"},

    {"pergunta": "Qual comando interrompe a execução de um laço antes do término natural da condição?",
     "alternativas": ["continue", "pass", "break", "return"],
     "correta": "C", "tema": "Estruturas de Repetição"},

    # Lista e matrizes
    {"pergunta": "Como acessamos o primeiro elemento de uma lista chamada numeros em Python?",
     "alternativas": ["numeros(0)", "numeros[1]", "numeros[0]", "numeros.first()"],
     "correta": "C", "tema": "Listas e Matrizes"},

    {"pergunta": "Na prática, o que é uma matriz em Python?",
     "alternativas": ["Um tipo de dado exclusivo chamado matriz", "Uma lista de listas",
                       "Uma funcao do Python", "Um dicionario obrigatorio"],
     "correta": "B", "tema": "Listas e Matrizes"},

    {"pergunta": "Qual função retorna a quantidade de elmentos de uma lista?",
     "alternativas": ["size()", "length()", "len()", "count_all()"],
     "correta": "C", "tema": "Listas e Matrizes"},

    {"pergunta": "Qual método adiciona um elemento ao final de uma lista?",
     "alternativas": ["lista.add()", "lista.append()", "lista.insert_end()", "lista.push()"],
     "correta": "B", "tema": "Listas e Matrizes"},

    {"pergunta": "Dada a matriz m = [[1, 2], [3, 4]], qual é o valor de m[1][0]?",
     "alternativas": ["1", "2", "3", "4"],
     "correta": "C", "tema": "Listas e Matrizes"},

    # Funções e modularização
    {"pergunta": "Qual palavra-chave é usada para definir uma função em Python?",
     "alternativas": ["function", "def", "func", "lambda"],
     "correta": "B", "tema": "Funções e Modularização"},

    {"pergunta": "Qual a principal vantagem de dividir um programa em funções (modularização)?",
     "alternativas": ["Tornar o codigo mais lento", "Organizar e reutilizar trechos de codigo",
                       "Impedir o uso de variaveis", "Aumentar o numero de erros"],
     "correta": "B", "tema": "Funções e Modularização"},

    {"pergunta": "O que a instrução return faz dentro de uma função?",
     "alternativas": ["Encerra o programa", "Devolve um valor e finaliza a execucao da funcao",
                       "Imprime um valor na tela", "Reinicia a funcao"],
     "correta": "B", "tema": "Funções e Modularização"},

    {"pergunta": "No código:\n  def soma(a, b):\n      return a + b\nQual o resultado de soma(2, 3)?",
     "alternativas": ["2", "3", "5", "Erro"],
     "correta": "C", "tema": "Funções e Modularização"},

    {"pergunta": "Os parâmetros de uma função servem para:",
     "alternativas": ["Armazenar comentarios do codigo", "Receber valores que a funcao usara internamente",
                       "Substituir a necessidade de variaveis", "Impedir que a funcao seja reutilizada"],
     "correta": "B", "tema": "Funções e Modularização"},
]

QUANTIDADE_PERGUNTAS_POR_PARTIDA = 10  # quantas perguntas (do banco de 25) entram em cada partida
LETRAS = ["A", "B", "C", "D"]  # usado para mapear índice da lista -> letra da alternativa



#Função responsável apenas por exibir o cabeçalho.
def exibir_cabecalho():
    print("=" * 50)
    print("       Quiz de preparação para a prova de Fund. de Computação e Algoritmos de Programação")
    print("=" * 50)

#Função que exibe as regras do jogo.
def exibir_regras():
    print("\n--- REGRAS DO QUIZ ---")
    print(f"- Serao sorteadas {QUANTIDADE_PERGUNTAS_POR_PARTIDA} perguntas de um banco de 25.")
    print("- Cada pergunta tem 4 alternativas: A, B, C ou D.")
    print("- Digite apenas a letra correspondente a alternativa escolhida.")
    print("- Ao final, voce vera sua pontuacao e um feedback sobre seu desempenho.")
    print("-----------------------\n")

# Lista de dicionarios com os dados dos criadores do quiz (nome + link do github).
# Usada pela funcao exibir_creditos() para montar a tela de creditos.
CRIADORES = [
    {"nome": "Davi Pimentel", "github": "https://github.com/daviribeiro-p"},
    {"nome": "Giuseppe Parrini", "github": "https://github.com/gparrini"},
    {"nome": "Mateus Alves", "github": "https://github.com/fateusmelipe"},
    {"nome": "Pedro Miclos", "github": "https://github.com/pedromiklos"},
]

#Função que exibe os créditos dos criadores do quiz.
def exibir_creditos():
    print("\n--- CREDITOS ---")
    print("Quiz desenvolvido por:")
    for criador in CRIADORES:  # laco for percorrendo a lista de criadores
        print(f"  - {criador['nome']} | GitHub: {criador['github']}")
    print("-----------------------\n")

# random.sample garante que as 10 perguntas sorteadas sejam diferentes entre
# si dentro da mesma partida, e o sorteio muda a cada execucao do programa.

def sortear_perguntas(banco, quantidade):
    perguntas_sorteadas = random.sample(banco, quantidade)  # nova lista com "quantidade" itens distintos
    return perguntas_sorteadas

# Lê a resposta do usuário e só aceita A, B, C ou D. Enquanto a entrada for
# invalida, o laco while continua pedindo novamente.

def ler_resposta_usuario():
    resposta = ""
    entrada_valida = False
    while not entrada_valida:  # repete ate o usuario digitar A, B, C ou D (aceita também minúscluo)
        resposta = input("Sua resposta (A/B/C/D): ").strip().upper()
        if resposta == "A" or resposta == "B" or resposta == "C" or resposta == "D":
            entrada_valida = True
        else:
            print(">> Entrada invalida! Digite apenas A, B, C ou D.\n")
    return resposta


# Aplica o quiz: percorre a lista de perguntas sorteadas, mostra cada uma,
# le a resposta do jogador e verifica se ela esta correta.

def jogar_quiz(perguntas):
    acertos = 0
    temas_errados = []  # lista que guarda os temas das perguntas que o jogador errou

    # percorre cada pergunta da lista sorteada
    for indice, pergunta_atual in enumerate(perguntas):
        print(f"\nPergunta {indice + 1} de {len(perguntas)}:")
        print(pergunta_atual["pergunta"])

        # mostra as alternativas (outro laço for, percorrendo a lista de alternativas)
        for i in range(len(pergunta_atual["alternativas"])):
            print(f"  {LETRAS[i]}) {pergunta_atual['alternativas'][i]}")

        resposta_usuario = ler_resposta_usuario()

        # compara a resposta do usuario com a correta
        if resposta_usuario == pergunta_atual["correta"]:
            print(">> Resposta correta!")
            acertos = acertos + 1
        elif resposta_usuario != pergunta_atual["correta"]:
            print(f">> Resposta incorreta. A alternativa correta era {pergunta_atual['correta']}.")
            temas_errados.append(pergunta_atual["tema"])  # guarda o tema para o feedback final
        else:
            # bloco else apenas para manter a estrutura completa de selecao
            print(">> Nao foi possivel avaliar a resposta.")
            # Davi:alguém remove esse else aqui, não precisa dele

    return acertos, temas_errados

# Mostra a pontuacao final e uma mensagem de feedback de acordo com o
# desempenho do jogador.
def mostrar_resultado(acertos, total, temas_errados):
    print("\n" + "=" * 50)
    print(f"Voce acertou {acertos} de {total} perguntas!")

    # mensagem de acordo com a pontuaçao
    if acertos == total:
        print("Excelente, voce esta pronto para a prova dia 10/06!")
    elif acertos >= total * 0.7:
        print("Muito bom! Voce domina a maior parte do conteudo.")
    elif acertos >= total * 0.4:
        print("Desempenho razoavel. Revise alguns pontos antes da prova dia 10/06.")
    else:
        print("Precisa revisar os materiais das aulas com mais atencao.")

    # se houve erros, lista os temas que precisam de revisão (sem repetir o mesmo tema)
    if len(temas_errados) > 0:
        temas_unicos = []
        for tema in temas_errados:  # laco for para montar a lista sem duplicados
            if tema not in temas_unicos:
                temas_unicos.append(tema)
        print("\nTemas que voce precisa revisar:")
        for tema in temas_unicos:
            print(f"  - {tema}")
    print("=" * 50)


# Exibe o menu principal e garante, com while + if/elif/else, que o usuário digite apenas uma opcao vailda (1, 2 ou 3).

def exibir_menu():
    print("\n----- MENU PRINCIPAL -----")
    print("1. Iniciar Jogo")
    print("2. Regras")
    print("3. Creditos")
    print("4. Sair")
    print("---------------------------")

    opcao = ""
    opcao_valida = False
    while not opcao_valida:  # repete enquanto a opcao digitada nao for 1, 2, 3 ou 4
        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            opcao_valida = True
        else:
            print(">> Opcao invalida! Digite 1, 2, 3 ou 4.")
    return opcao

# Função principal: organiza o fluxo do programa.
# mantem o menu rodando até o jogador sair.

def main():
    exibir_cabecalho()
    rodando = True

    while rodando:  # laco while que mantem o menu principal ativo
        opcao_escolhida = exibir_menu()

        # navegacao do menu principal
        if opcao_escolhida == "1":
            perguntas_da_partida = sortear_perguntas(BANCO_PERGUNTAS, QUANTIDADE_PERGUNTAS_POR_PARTIDA)
            acertos, temas_errados = jogar_quiz(perguntas_da_partida)
            mostrar_resultado(acertos, len(perguntas_da_partida), temas_errados)
        elif opcao_escolhida == "2":
            exibir_regras()
        elif opcao_escolhida == "3":
            exibir_creditos()
        elif opcao_escolhida == "4":
            print("\nEncerrando o quiz. Bons estudos!")
            rodando = False  # condicao que fara o while terminar
        else:
            print("Opcao desconhecida.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()