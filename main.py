import yfinance as yf


SPX = "PSP5.PA"
NDX = "PUST.PA"
SP2 = "CL2.PA"
ND2 = "LQQ.PA"

PORTFOLIO = {"CL2.PA", "NVDA", "MSFT", "GOOGL", "ASML.AS", "AMZN",}

BUYS = {2025 : [],}


if __name__ == "__main__":
    benchmark = yf.Ticker(SPX)
    historical_data = benchmark.history(period = "1y")
    print(historical_data)
    pass