# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.
    
    A função assume a data de nascimento como 1º de janeiro do ano fornecido
    e calcula a diferença até a data de hoje.

    Parâmetros:
        ano_nascimento (int): O ano em que a pessoa nasceu (ex: 1990).

    Retorna:
        int: O número total de dias vividos.
        
    Levanta:
        ValueError: Se o ano de nascimento for inválido ou estiver no futuro.
    """
    
    # 1. Obter a data e hora de hoje
    hoje = datetime.now()
    
    # 2. Obter o ano atual para validação
    ano_atual = hoje.year

    # 3. Validar a entrada
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode estar no futuro.")
    if ano_nascimento <= 0:
        raise ValueError("O ano de nascimento parece ser inválido (menor ou igual a zero).")

    # 4. Definir a data de nascimento (assumindo 1º de janeiro do ano)
    #    Usamos datetime(ano, mes, dia)
    try:
        data_nascimento = datetime(ano_nascimento, 1, 1)
    except ValueError:
        # Pega anos inválidos que o datetime possa rejeitar (ex: ano 0)
        raise ValueError("Ano de nascimento inválido.")
        
    # 5. Calcular a diferença entre as datas
    #    A subtração de dois objetos datetime resulta em um objeto 'timedelta'
    diferenca_tempo = hoje - data_nascimento
    
    # 6. Retornar apenas a parte 'dias' do timedelta
    return diferenca_tempo.days

# --- Bloco Principal de Execução ---
# Este código só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    
    print("--- Calculadora de Idade em Dias ---")
    
    try:
        # 1. Obter a entrada do usuário
        ano_str = input("Digite o ano do seu nascimento (ex: 1990): ")
        
        # 2. Converter a entrada para inteiro
        ano = int(ano_str)
        
        # 3. Chamar a função
        dias_vividos = calcular_idade_em_dias(ano)
        
        # 4. Exibir o resultado
        #    O ':,' formata o número com separadores de milhar (ex: 9.132)
        print("\n--- Resultado ---")
        print(f"Você nasceu em {ano}.")
        print(f"Considerando a data de hoje ({hoje.strftime('%d/%m/%Y')}),")
        print(f"Você viveu aproximadamente {dias_vividos:,'} dias.")

    except ValueError as e:
        # Captura erros de digitação (ex: 'abc') E
        # erros da nossa função (ex: ano no futuro)
        print(f"\n[ERRO]: {e}")
        print("Por favor, insira um ano válido.")
        
    except Exception as e:
        # Pega qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO]: {e}")