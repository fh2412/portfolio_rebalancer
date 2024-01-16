import gradio as gr

def perfect_rebalance(stocks, ltbonds, mtbonds, gold, com):
    print(stocks, ltbonds, mtbonds, gold, com)
    """
    Rebalance the portfolio to match the target allocation perfectly.

    Parameters:
    - all_season_portfolio (dict): Target allocation percentages for each asset class.
    - current_values (dict): Current values of each asset class in the portfolio.

    Returns:
    - updated_values (dict): Updated values of each asset class after rebalancing.
    - updated_weights (dict): Updated weights of each asset class after rebalancing.
    """
    stocks = float(stocks)
    ltbonds = float(ltbonds)
    mtbonds = float(mtbonds)
    gold = float(gold)
    com = float(com)
    
    current_values = {
        'Stocks': stocks,  # replace with your actual value
        'Long_Term_Bonds': ltbonds,
        'Intermediate_Term_Bonds': mtbonds,
        'Gold': gold,
        'Commodities': com
    }
    all_season_portfolio = {
        'Stocks': 0.3,
        'Long_Term_Bonds': 0.4,
        'Intermediate_Term_Bonds': 0.15,
        'Gold': 0.075,
        'Commodities': 0.075
    }

    print(current_values)
    total_current_value = sum(current_values.values())

    # Calculate adjustments
    adjustments = {asset: all_season_portfolio[asset] * total_current_value - value for asset, value in current_values.items()}

    # Update current values
    updated_values = {asset: value + adjustments[asset] for asset, value in current_values.items()}

    # Recalculate weights after the transfer
    total_updated_value = sum(updated_values.values())
    updated_weights = {asset: value / total_updated_value for asset, value in updated_values.items()}

    # Format result string for display
    result_str = "Updated Portfolio Values:\n"
    for asset, value in updated_values.items():
        result_str += f"{asset}: ${value:.2f} (Rebalance: ${adjustment:.2f})\n"

    result_str += "\nUpdated Portfolio Weights:\n"
    for asset, weight in updated_weights.items():
        result_str += f"{asset}: {weight:.2%}\n"

    return result_str

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
        gr.Textbox("Rebalance Result", type="text")
    ]
)

# Launch the Gradio interface
iface.launch()