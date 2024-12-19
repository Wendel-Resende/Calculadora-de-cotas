"""
Module for Streamlit UI configuration and constants.
"""

# Input field configurations
PRICE_INPUT_CONFIG = {
    "min_value": 0.01,
    "step": 0.01,
    "format": "%.2f"
}

QUANTITY_INPUT_CONFIG = {
    "min_value": 1,
    "step": 1
}

# UI Text
TITLE = "Calculadora de Preço Médio"
DESCRIPTION = "Calcule quantas cotas ou ações adicionais você precisa comprar para alcançar o preço médio desejado."

# Input Labels
CURRENT_PRICE_LABEL = "Preço Atual da Cota/Ação"
CURRENT_QUANTITY_LABEL = "Quantidade Atual de Cotas/Ação"
CURRENT_AVERAGE_LABEL = "Preço Médio Atual"
DESIRED_AVERAGE_LABEL = "Preço Médio Desejado"
CALCULATE_BUTTON_LABEL = "Calcular"
