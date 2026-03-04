
def stock_tracker():
   
    # 1. Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180,    # Apple
        "TSLA": 250,    # Tesla
        "GOOGL": 140,   # Google
        "AMZN": 175,    # Amazon
        "MSFT": 400,    # Microsoft
        "META": 290,    # Meta (Facebook)
        "NFLX": 480,    # Netflix
        "NVDA": 820     # NVIDIA
    }

    # Display welcome message and available stocks
    print("=" * 50)
    print("     STOCK PORTFOLIO TRACKER v1.0")
    print("=" * 50)
    print("\nAvailable stocks and their current prices:")
    print("-" * 40)
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price}")
    print("-" * 40)

    # Initialize portfolio storage
    portfolio = []
    total_value = 0
    stock_count = 0

    # 2. User Input Loop
    print("\n" + "=" * 50)
    print("ENTER YOUR STOCK HOLDINGS")
    print("(Type 'done' when finished)")
    print("=" * 50 + "\n")

    while True:
        # Get stock symbol from user
        symbol = input("Enter stock symbol: ").upper().strip()
        
        # Check if user wants to finish
        if symbol == 'DONE':
            break
        
        # Validate stock symbol
        if symbol in stock_prices:
            try:
                # Get quantity from user
                quantity_input = input(f"How many shares of {symbol} do you own? ")
                quantity = int(quantity_input)
                
                # Validate quantity is positive
                if quantity <= 0:
                    print("Please enter a positive number of shares.\n")
                    continue
                
                # Calculate investment value
                price = stock_prices[symbol]
                investment = quantity * price
                
                # Store data for the report
                portfolio.append({
                    'symbol': symbol,
                    'quantity': quantity,
                    'price': price,
                    'investment': investment
                })
                
                # Update totals
                total_value += investment
                stock_count += 1
                
                print(f"Added {quantity} shares of {symbol} at ${price} = ${investment:,.2f}\n")
                
            except ValueError:
                print(" Invalid quantity. Please enter a whole number.\n")
        else:
            print(f"Stock '{symbol}' not found in database.")
            print(f"   Available stocks: {', '.join(stock_prices.keys())}\n")

    # 3. Display Results
    print("\n" + "=" * 50)
    print("         YOUR PORTFOLIO SUMMARY")
    print("=" * 50)

    if stock_count == 0:
        print("\nNo stocks in portfolio.\n")
    else:
        print("\n" + "-" * 50)
        print(f"{'Symbol':<8} {'Shares':<10} {'Price':<10} {'Investment':<15}")
        print("-" * 50)
        
        for item in portfolio:
            print(f"{item['symbol']:<8} {item['quantity']:<10} ${item['price']:<9} ${item['investment']:<14,.2f}")
        
        print("-" * 50)
        print(f"{'TOTAL':<8} {'':<10} {'':<10} ${total_value:<14,.2f}")
        print(f"\n Total Holdings: {stock_count}")
        print("=" * 50)

    # 4. Optional: Save to File
    if stock_count > 0:
        save_choice = input("\nWould you like to save this report to a file? (y/n): ").lower().strip()
        
        if save_choice == 'y':
            # Ask for file format preference
            print("\nChoose file format:")
            print("1. Text file (.txt)")
            print("2. CSV file (.csv)")
            format_choice = input("Enter choice (1 or 2): ").strip()
            
            if format_choice == '1':
                save_as_txt(portfolio, total_value, stock_count)
            elif format_choice == '2':
                save_as_csv(portfolio, total_value)
            else:
                print("Invalid choice. File not saved.")
    else:
        print("\nNo portfolio data to save.")

def save_as_txt(portfolio, total_value, stock_count):
    """
    Save portfolio data as a formatted text file.
    """
    filename = "portfolio_report.txt"
    
    try:
        with open(filename, "w") as f:
            # Write header
            f.write("=" * 50 + "\n")
            f.write("     STOCK PORTFOLIO REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            # Write date
            from datetime import datetime
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Write table header
            f.write("-" * 50 + "\n")
            f.write(f"{'Symbol':<8} {'Shares':<10} {'Price':<10} {'Investment':<15}\n")
            f.write("-" * 50 + "\n")
            
            # Write each stock
            for item in portfolio:
                f.write(f"{item['symbol']:<8} {item['quantity']:<10} ${item['price']:<9} ${item['investment']:<14,.2f}\n")
            
            # Write totals
            f.write("-" * 50 + "\n")
            f.write(f"{'TOTAL':<8} {'':<10} {'':<10} ${total_value:<14,.2f}\n\n")
            f.write(f"Total Holdings: {stock_count}\n")
            f.write("=" * 50)
        
        print(f"Report saved to '{filename}'!")
        
        # Show preview
        print("\n File preview:")
        print("-" * 30)
        with open(filename, "r") as f:
            for i, line in enumerate(f):
                if i < 5:  # Show first 5 lines
                    print(line.rstrip())
        print("...")
        
    except Exception as e:
        print(f" Error saving file: {e}")

def save_as_csv(portfolio, total_value):
    """
    Save portfolio data as a CSV file for Excel/ spreadsheet use.
    """
    filename = "portfolio_report.csv"
    
    try:
        with open(filename, "w") as f:
            # Write header
            f.write("Symbol,Quantity,Price,Investment\n")
            
            # Write each stock
            for item in portfolio:
                f.write(f"{item['symbol']},{item['quantity']},{item['price']},{item['investment']}\n")
            
            # Write total
            f.write(f"TOTAL,,,{total_value}\n")
        
        print(f"Report saved to '{filename}'!")
        print("   This file can be opened in Excel or any spreadsheet program.")
        
    except Exception as e:
        print(f" Error saving file: {e}")

# Run the program
if __name__ == "__main__":
    stock_tracker()