# =============================================================================
# DIVISÃO 1: MEMBRO 1 - Estrutura de Dados e Banco de Perguntas
# Responsabilidade: Explicar a estrutura da matriz (lista de dicionários),
# como as perguntas estão organizadas por tema e como a estrutura de dados
# permite que o jogo funcione de forma dinâmica.
# =============================================================================
BANCO_PERGUNTAS = [ ... ] # (Todo o bloco do banco)

QUANTIDADE_PERGUNTAS_POR_PARTIDA = 10
LETRAS = ["A", "B", "C", "D"]


# =============================================================================
# DIVISÃO 2: MEMBRO 2 - Módulos de Exibição e Menu
# Responsabilidade: Explicar as funções de interface (exibir_cabecalho, 
# exibir_regras, exibir_menu). Focar em como o 'while' e o 'if/else' 
# garantem que o usuário navegue corretamente pelo menu.
# =============================================================================
def exibir_cabecalho(): ...
def exibir_regras(): ...
def exibir_menu(): ...


# =============================================================================
# DIVISÃO 3: MEMBRO 3 - Lógica de Sorteio e Entrada de Dados
# Responsabilidade: Explicar a função sortear_perguntas (uso do módulo random) 
# e a função ler_resposta_usuario (validação de entrada). Explicar por que
# usar 'while' aqui é vital para evitar erros de digitação do usuário.
# =============================================================================
def sortear_perguntas(banco, quantidade): ...
def ler_resposta_usuario(): ...


# =============================================================================
# DIVISÃO 4: MEMBRO 4 - Lógica do Quiz e Controle Principal
# Responsabilidade: Explicar o coração do programa (jogar_quiz e mostrar_resultado). 
# Focar em como o 'for' percorre a lista de perguntas e como a lógica de
# acertos/erros (temas_errados) monta o feedback final. Explicar o 'main()'.
# =============================================================================
def jogar_quiz(perguntas): ...
def mostrar_resultado(acertos, total, temas_errados): ...
def main(): ...