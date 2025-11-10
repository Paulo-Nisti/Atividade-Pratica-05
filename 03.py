# Crie um programa que receba o preço original de um produto e um percentual de desconto, 
# realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
# Permitir que o usuário informe o preço do produto e o percentual de desconto.
# Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# Exibir o preço final com duas casas decimais para garantir precisão. 
# Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

def calcular_preco_final():
    """
    Solicita ao usuário o preço original e o percentual de desconto,
    e calcula o preço final após o desconto.
    Exibe o resultado com duas casas decimais.
    """
    
    print("--- Calculadora de Preço com Desconto ---")
    
    try:
        # 1. Obter entradas do usuário
        preco_original_str = input("Digite o preço original do produto (ex: 250.75): ")
        preco_original = float(preco_original_str)
        
        percentual_desconto_str = input("Digite o percentual de desconto (ex: 10): ")
        percentual_desconto = float(percentual_desconto_str)

        # 2. Validar entradas
        if preco_original < 0 or percentual_desconto < 0:
            print("\n[ERRO] Os valores inseridos não podem ser negativos.")
            return # Para a execução da função se a entrada for inválida

        # 3. Calcular o valor do desconto
        #    (ex: 10% de 250.75 -> (10 / 100) * 250.75 = 25.075)
        valor_desconto = (percentual_desconto / 100) * preco_original
        
        # 4. Calcular o preço final
        preco_final = preco_original - valor_desconto
        
        # 5. Exibir os resultados formatados com duas casas decimais
        #    O formato ':.2f' garante a exibição de valores monetários
        print("\n--- Resumo ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto ({percentual_desconto:.0f}%): R$ {valor_desconto:.2f}")
        print("----------------------------")
        print(f"Preço Final:    R$ {preco_final:.2f}")

    except ValueError:
        # Captura erro se o usuário digitar "abc" ou "dez%" em vez de um número
        print("\n[ERRO] Entrada inválida. Por favor, insira apenas números.")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO]: {e}")

# --- Ponto de Entrada do Programa ---
# O código abaixo só é executado quando o script é rodado diretamente
if __name__ == "__main__":
    calcular_preco_final()