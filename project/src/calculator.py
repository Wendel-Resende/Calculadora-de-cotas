"""
Module for calculating average price and required shares.
"""

def calculate_new_shares(current_price: float, current_quantity: int, 
                        current_average: float, desired_average: float) -> str:
    """
    Calculate how many additional shares need to be purchased to reach a desired average price.

    Args:
        current_price (float): Current price per share
        current_quantity (int): Current number of shares owned
        current_average (float): Current average price per share
        desired_average (float): Target average price per share

    Returns:
        str: Message indicating the number of shares to purchase and total investment needed,
             or an error message
    """
    # Validate input
    if desired_average <= current_price:
        return "O preço médio desejado deve ser maior que o preço atual."

    # Calculate total investment so far
    total_invested = current_quantity * current_average

    # Calculate required new shares
    new_quantity = (total_invested - (current_quantity * desired_average)) / (desired_average - current_price)

    if new_quantity > 0:
        # Calculate total investment needed
        investment_needed = new_quantity * current_price
        return (
            f"Você precisa comprar {new_quantity:.2f} cotas adicionais.\n"
            f"Investimento necessário: R$ {investment_needed:.2f}"
        )
    else:
        return "Não é possível alcançar o preço médio desejado com compras ao preço atual."
