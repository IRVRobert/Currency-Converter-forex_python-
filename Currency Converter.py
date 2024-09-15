from forex_python.converter import CurrencyRates
from forex_python.converter import RatesNotAvailableError

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        return c.convert(from_currency, to_currency, amount)
    except RatesNotAvailableError:
        print("Currency rate not available for the given currencies.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()
        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    except ValueError:
        print("Invalid amount entered. Please enter a numerical value.")