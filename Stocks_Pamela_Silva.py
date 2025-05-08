#https://www.alphavantage.co/support/#api-key

def fetch_daily_stock_prices(api_key, ticker_symbol):
    import requests
    # Define the endpoint URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={api_key}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the time series data
        time_series = data.get("Time Series (Daily)", {})
        
        # Print the daily stock prices
        for date, prices in time_series.items():
            print(f"Date: {date}")
            print(f"Open: {prices['1. open']}")
            print(f"High: {prices['2. high']}")
            print(f"Low: {prices['3. low']}")
            print(f"Close: {prices['4. close']}")
            print(f"Volume: {prices['5. volume']}")
            print("-" * 20)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


def fetch_latest_stock_price(api_key, ticker_symbol):
    import requests
    # Define the endpoint URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker_symbol}&apikey={api_key}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the time series data
        time_series = data.get("Time Series (Daily)", {})
        
        # Get the latest date
        latest_date = max(time_series.keys())
        
        # Get the latest stock prices
        latest_prices = time_series[latest_date]
        print("Raw Data:", latest_prices)
        
        # Print the latest stock prices
        print(f"Latest Date: {latest_date}")
        print(f"Open: {latest_prices['1. open']}")
        print(f"High: {latest_prices['2. high']}")
        print(f"Low: {latest_prices['3. low']}")
        print(f"Close: {latest_prices['4. close']}")
        print(f"Volume: {latest_prices['5. volume']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        
def main():
    
    api_key = "your_api_key"
    ticker_symbol = input("Enter ticker symbol: ")
    #fetch_daily_stock_prices(api_key, ticker_symbol)

    fetch_latest_stock_price(api_key, ticker_symbol)

main()
    
    api_key = "your_api_key"
    ticker_symbol = input("Enter ticker symbol: ")
    #fetch_daily_stock_prices(api_key, ticker_symbol)

    fetch_latest_stock_price(api_key, ticker_symbol)

main()