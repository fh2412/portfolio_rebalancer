import gradio as gr

def perfect_rebalance(all_season_portfolio, current_values):
    """
    Rebalance the portfolio to match the target allocation perfectly.

    Parameters:
    - all_season_portfolio (dict): Target allocation percentages for each asset class.
    - current_values (dict): Current values of each asset class in the portfolio.

    Returns:
    - updated_values (dict): Updated values of each asset class after rebalancing.
    - updated_weights (dict): Updated weights of each asset class after rebalancing.
    """
    total_current_value = sum(current_values.values())

    # Calculate adjustments
    adjustments = {asset: all_season_portfolio[asset] * total_current_value - value for asset, value in current_values.items()}

    # Update current values
    updated_values = {asset: value + adjustments[asset] for asset, value in current_values.items()}

    # Recalculate weights after the transfer
    total_updated_value = sum(updated_values.values())
    updated_weights = {asset: value / total_updated_value for asset, value in updated_values.items()}

    return updated_values, updated_weights

# Define the Gradio interface
iface = gr.Interface(
    fn=perfect_rebalance,
    inputs=[
        gr.Textbox("Stocks", type="text"),
        gr.Textbox("Long_Term_Bonds", type="text"),
        gr.Textbox("Intermediate_Term_Bonds", type="text"),
        gr.Textbox("Gold", type="text"),
        gr.Textbox("Commodities", type="text"),
    ],
    outputs=[
        gr.Textbox("Updated Portfolio Values"),
        gr.Textbox("Updated Portfolio Weights")
    ]
)

# Launch the Gradio interface
iface.launch()