import requests

def get_crypto_price(crypto_id):
    crypto_id = input("Enter the name of the cryptocurrency: ")
    url = f"https://api.coincap.io/v2/assets/{crypto_id}"
    response = requests.get(url)
    data = response.json()
    price = float(data['data']['priceUsd'])
    print(f"The price of {crypto_id} is ${price:,.2f}")
    return

if __name__ == "__main__":
    get_crypto_price('bitcoin')