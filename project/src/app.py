"""
Main application file for the Average Price Calculator.
"""

import streamlit as st
from calculator import calculate_new_shares
from ui_config import (
    PRICE_INPUT_CONFIG,
    QUANTITY_INPUT_CONFIG,
    TITLE,
    DESCRIPTION,
    CURRENT_PRICE_LABEL,
    CURRENT_QUANTITY_LABEL,
    CURRENT_AVERAGE_LABEL,
    DESIRED_AVERAGE_LABEL,
    CALCULATE_BUTTON_LABEL
)

def main():
    """Main function to run the Streamlit application."""
    # Set up the page
    st.title(TITLE)
    st.write(DESCRIPTION)

    # Input fields
    current_price = st.number_input(
        CURRENT_PRICE_LABEL,
        **PRICE_INPUT_CONFIG
    )
    
    current_quantity = st.number_input(
        CURRENT_QUANTITY_LABEL,
        **QUANTITY_INPUT_CONFIG
    )
    
    current_average = st.number_input(
        CURRENT_AVERAGE_LABEL,
        **PRICE_INPUT_CONFIG
    )
    
    desired_average = st.number_input(
        DESIRED_AVERAGE_LABEL,
        **PRICE_INPUT_CONFIG
    )

    # Calculate button
    if st.button(CALCULATE_BUTTON_LABEL):
        result = calculate_new_shares(
            current_price,
            current_quantity,
            current_average,
            desired_average
        )
        st.write(result)

if __name__ == "__main__":
    main()