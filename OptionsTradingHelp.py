import yfinance as yf

def get_stock_info(symbol):
    
    stock_data = yf.Ticker(symbol)
    
    # Fetching historical data
    hist_prev_day = stock_data.history(period='1d')
    hist_prev_week = stock_data.history(period='1wk')
    
    # Today's open price
    open_price = hist_prev_day['Open'][0]
    
    # Pre-market high and low
    pre_market_high = max(hist_prev_day['High'])
    pre_market_low = min(hist_prev_day['Low'])
    
    # Previous day's open, high, and low
    prev_day_open = hist_prev_day['Open'][-1]
    prev_day_high = max(hist_prev_day['High'])
    prev_day_low = min(hist_prev_day['Low'])
    
    # Previous week's high and low
    prev_week_high = max(hist_prev_week['High'])
    prev_week_low = min(hist_prev_week['Low'])
    
    print("Today's Open Price:", open_price)
    print("Pre-Market High:", pre_market_high)
    print("Pre-Market Low:", pre_market_low)
    print("Previous Day's Open:", prev_day_open)
    print("Previous Day's High:", prev_day_high)
    print("Previous Day's Low:", prev_day_low)
    print("Previous Week's High:", prev_week_high)
    print("Previous Week's Low:", prev_week_low)
    
# Example usage

get_stock_info("QQQ")
