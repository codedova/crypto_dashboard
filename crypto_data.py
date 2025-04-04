import requests

def fetch_crypto_data(vs_currency="usd", per_page=10, page=1):
    """
    Fetch cryptocurrency market data from CoinGecko.
    
    Args:
        vs_currency (str): Currency to compare (default 'usd').
        per_page (int): Number of coins per page.
        page (int): Page number to fetch.
    
    Returns:
        List of dictionaries containing crypto market data.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    return response.json()

if __name__ == "__main__":
    # Test: fetch data for top 5 cryptocurrencies
    data = fetch_crypto_data(per_page=5)
    for coin in data:
        print(coin["id"], coin["current_price"])
