# Remove the non-numerics…
def parse_currency(amount_str):
    cleaned_amount = ''.join(c for c in amount_str if c.isdigit() or c == '.')
    return float(cleaned_amount)

def parse_percentage(percentage_str):
    cleaned_percentage = ''.join(c for c in percentage_str if c.isdigit() or c == '.')
    return float(cleaned_percentage)

# Input
price_input = input("Enter the price (e.g., $100.00): ")
percentage_input = input("Enter the tipping percentage (e.g., 15%): ")

# Parse inputs
price = parse_currency(price_input)
percentage = parse_percentage(percentage_input)

# Calculate the tip
tip = (price * percentage) / 100

# Print the tip amount
print(f"Please leave ${tip:.2f}")

