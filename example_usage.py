portfolio = generate_portfolio(risk_level="Moderate", investment_amount=10000)
for entry in portfolio:
    print(f"{entry['asset_class']}\t{entry['ticker']}\t${entry['allocation']:.2f}")