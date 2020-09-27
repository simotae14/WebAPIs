import requests

# define method main
def main():
    #response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP")
    payload = {
        'base': 'USD',
        'symbols': 'GBP'
    }
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("The API request doesn't finish well!")
    data = response.json()
    print("JSON data: ", data)
if __name__ == "__main__":
    main()
