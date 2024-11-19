import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coincap.io/v2/assets/{crypto_id}"
    response = requests.get(url)
    data = response.json()
    price = data['data']['priceUsd']
    return price

# Example usage
crypto_id = 'ethereum'
price = get_crypto_price(crypto_id)
print(f"The price of {crypto_id} is ${price}")