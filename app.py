import requests

def get_crypto_price():
    crypto_id = input("Enter the name of the cryptocurrency: ")
    url = f"https://api.coincap.io/v2/assets/{crypto_id}"
    response = requests.get(url)
    data = response.json()
    price = float(data['data']['priceUsd'])
    print(f"The price of {crypto_id} is ${price:,.2f}")
    return

if __name__ == "__main__":
    print("---Welcome to the Cryptocurrency Price Checker---")
    print("This program will give you the current price of any cryptocurrency you want.")
    print("")
    while True:
        print("1. Get the price of a cryptocurrency (name not on capital letters)")
        action = input("What you want to do? (Enter 'quit' to exit): ")
        if action == 'quit':
            break
        else:
            match action:
                case '1':
                    actions_passed = False
                    while actions_passed == False:
                        try:
                            get_crypto_price()
                            actions_passed = True
                        except KeyError:
                            print("Invalid Cyptocurrency Name. Please try again.")
