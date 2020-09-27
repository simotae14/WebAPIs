import requests

# define method main
def main():
    response = requests.get("http://www.google.com")
    print("Status code: ", response.status_code)
    #print("Headers: ", response.headers)
    #print("Content Type: ", response.headers["Content-Type"])
    print("Content: ", response.text)

if __name__ == "__main__":
    main()
