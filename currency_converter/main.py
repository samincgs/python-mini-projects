# a simple command line currency converter. The program has a dictionary of exchange rates and utilizes it to convert the user's currency
from sys import exit

exchange_rates = {
    "USD": (1.0, "United States Dollar"),
    "EUR": (0.85, "Euro"),
    "GBP": (0.73, "Pound sterling"),
    "JPY": (110.29, "Japanese Yen"),
    "INR": (73.5, "Indian Rupee"),
}


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    if (
        from_currency not in exchange_rates.keys()
        or to_currency not in exchange_rates.keys()
    ):
        return "Invalid currency."

    rate = exchange_rates[to_currency][0] / exchange_rates[from_currency][0]
    conversion = amount * rate
    return conversion


def main():
    print("\nCurrency Converter\n")
    print(
        """-------------------------------
Currencies available:
USD, EUR, GBP, JPY, INR
-------------------------------\n"""
    )
    from_currency = input(
        "Please choose the currency you want to convert from: "
    ).upper()
    to_currency = input("Please choose the currency you want to convert to: ").upper()

    if from_currency == to_currency:
        print("\nSource and target currencies are the same. \nPlease try again:)")
        exit()

    if (
        from_currency not in exchange_rates.keys()
        or to_currency not in exchange_rates.keys()
    ):
        print("\nInvalid currency choice.\nPlease try again:)")
        exit()

    amount = float(input("What is the amount of money you want to convert: "))
    converted = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted, str):
        print(converted)
    else:
        print(
            f"Exchange rate:\n{exchange_rates[from_currency][0]} {exchange_rates[from_currency][1]} = {exchange_rates[to_currency][0]} {exchange_rates[to_currency][1]}"
        )
        print(
            f"\nCurrency Converted:\n{amount:.2f} {from_currency} is equal to {converted:.2f} {to_currency}"
        )


if __name__ == "__main__":
    main()
