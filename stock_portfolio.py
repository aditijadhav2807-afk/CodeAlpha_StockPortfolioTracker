# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2

# Predefined stock prices (sample prices)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when finished.")

# Take stock name and quantity from user
while True:
    stock = input("\nEnter stock name: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Add quantity if the stock is entered again
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate and display portfolio
print("\n" + "=" * 40)
print("       YOUR STOCK PORTFOLIO")
print("=" * 40)

if not portfolio:
    print("No stocks were added.")

else:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        print(f"\nStock: {stock}")
        print(f"Quantity: {quantity}")
        print(f"Price per share: ${price}")
        print(f"Investment: ${investment}")

    print("\n" + "-" * 40)
    print(f"Total Investment: ${total_investment}")

    # Save portfolio to a text file
    save = input("\nSave result to file? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("-" * 30 + "\n")

            for stock, quantity in portfolio.items():
                investment = stock_prices[stock] * quantity
                file.write(
                    f"{stock} - Quantity: {quantity}, "
                    f"Investment: ${investment}\n"
                )

            file.write(
                f"\nTotal Investment: ${total_investment}\n"
            )

        print("Portfolio saved to portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")