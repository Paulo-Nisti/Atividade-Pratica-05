# Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
# baseada no valor total da conta e na porcentagem de gorjeta desejada. 
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros: valor_conta (float): 
# O valor total da conta porcentagem_gorjeta (float): 
# A porcentagem da gorjeta (ex: 15 para 15%)
# Retorna: float: O valor da gorjeta calculada


def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta (ex: 150.50).
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
        
    Levanta:
        ValueError: Se o valor da conta ou a porcentagem da gorjeta forem negativos.
    """
    
    # Validação de entrada: valores não podem ser negativos
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
        
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")

    # Cálculo principal:
    # Converte a porcentagem (ex: 15) para seu valor decimal (0.15)
    valor_decimal_gorjeta = porcentagem_gorjeta / 100
    
    # Calcula o valor da gorjeta
    valor_da_gorjeta = valor_conta * valor_decimal_gorjeta
    
    return valor_da_gorjeta

# --- Bloco Principal de Execução ---
# Este código só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    
    print("--- Calculadora de Gorjeta de Restaurante ---")
    
    try:
        # 1. Obter entradas do usuário
        # Usamos float() para converter a entrada de texto em um número
        entrada_conta = input("Digite o valor total da conta: R$ ")
        conta = float(entrada_conta)
        
        entrada_porcentagem = input("Digite a porcentagem de gorjeta desejada (ex: 15): % ")
        porcentagem = float(entrada_porcentagem)
        
        # 2. Chamar a função com os valores
        gorjeta_calculada = calcular_gorjeta(conta, porcentagem)
        
        # 3. Calcular o total final
        total_a_pagar = conta + gorjeta_calculada
        
        # 4. Exibir os resultados formatados (:.2f) para 2 casas decimais
        print("\n--- Resumo da Conta ---")
        print(f"Valor da Conta: R$ {conta:.2f}")
        print(f"Gorjeta ({porcentagem:.0f}%): R$ {gorjeta_calculada:.2f}")
        print("-" * 25)
        print(f"Total a Pagar:  R$ {total_a_pagar:.2f}")

    except ValueError as e:
        # Captura erros de digitação (ex: 'abc') E
        # erros da nossa função (ex: valores negativos)
        print(f"\n[ERRO]: {e}")
        print("Por favor, insira valores numéricos válidos e positivos.")
        
    except Exception as e:
        # Pega qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO]: {e}")