# Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
# Crie um programa que receba o preço original de um produto e um percentual de desconto, 
# realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
# Permitir que o usuário informe o preço do produto e o percentual de desconto.
# Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# Exibir o preço final com duas casas decimais para garantir precisão. 
# Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

import re

# --- Parte 1: Verificador de Palíndromo ---

def verificar_palindromo(frase: str):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e diferenças de maiúsculas/minúsculas.
    
    Imprime "Sim" se for um palíndromo, ou "Não" caso contrário.
    """
    
    # 1. Normalizar a string:
    #    - Converte tudo para minúsculas com .lower()
    #    - Remove tudo que NÃO for uma letra ou número (a-z, 0-9)
    #      usando uma expressão regular (re.sub)
    frase_limpa = re.sub(r'[^a-z0-9]', '', frase.lower())
    
    # 2. Verificar se a string limpa é igual à sua inversa
    #    (string[::-1] é um truque do Python para inverter a string)
    if frase_limpa == frase_limpa[::-1]:
        print("Sim")
    else:
        print("Não")

# --- Parte 2: Calculadora de Desconto ---

def calcular_preco_final():
    """
    Solicita ao usuário o preço original e o percentual de desconto,
    e calcula o preço final após o desconto.
    Exibe o resultado com duas casas decimais.
    """
    
    print("--- Calculadora de Desconto ---")
    
    try:
        # 1. Obter entradas do usuário
        preco_original_str = input("Digite o preço do produto (ex: 250.75): ")
        preco_original = float(preco_original_str)
        
        percentual_desconto_str = input("Digite o percentual de desconto (ex: 10): ")
        percentual_desconto = float(percentual_desconto_str)

        # Validação para evitar números negativos
        if preco_original < 0 or percentual_desconto < 0:
            print("\n[ERRO] Os valores inseridos não podem ser negativos.")
            return # Para a execução da função
            
        # 2. Calcular o valor do desconto
        #    (ex: 10% de 250.75 -> (10 / 100) * 250.75 = 25.075)
        valor_desconto = (percentual_desconto / 100) * preco_original
        
        # 3. Calcular o preço final
        preco_final = preco_original - valor_desconto
        
        # 4. Exibir o resultado formatado
        print("\n--- Resultado ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")

    except ValueError:
        # Captura erro se o usuário digitar "abc" em vez de um número
        print("\n[ERRO] Entrada inválida. Por favor, insira apenas números.")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"\n[ERRO INESPERADO]: {e}")

# --- Bloco de Execução Principal ---
# (Isso permite que o arquivo seja executado)
if __name__ == "__main__":
    
    # 1. Testando a função de palíndromo
    print("--- Teste do Verificador de Palíndromo ---")
    verificar_palindromo("Ovo")
    verificar_palindromo("Anota aí: Atibaia, na Toca.")
    verificar_palindromo("Isso não é um palíndromo")
    
    print("\n" + "="*40 + "\n")
    
    # 2. Executando a calculadora de desconto
    calcular_preco_final()