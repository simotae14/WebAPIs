import requests

# define method main
def main():
    #response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP")
    first_currency = input("Insert your first currency: ")
    second_currency = input("Insert your second currency: ")

    payload = {
        'base': first_currency,
        'symbols': second_currency
    }
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("The API request doesn't finish well!")
    response_data = response.json()
    rate_exchange = response_data["rates"][second_currency]
    print("Data: ", response_data["date"])
    print(f"1 {first_currency} is equal to {rate_exchange} {second_currency}")
if __name__ == "__main__":
    main()
