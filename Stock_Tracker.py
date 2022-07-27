import requests
import pandas as pd
import finnhub
import datetime as dt
import plotly.graph_objects as go


finnhub_client = finnhub.Client(api_key="cbg8252ad3i4ro62488g")

res = finnhub_client.stock_candles("AAPL", "D", 1577926800, 1658620800)

df = pd.DataFrame(res)
df = df.rename(columns={'c':"Close", 'h':"High", 'l':"Low", 'o':"Open", 's':"Status", 't':"Date", 'v':"Volume"})
df["Date"] = df["Date"].apply(lambda x: dt.datetime.fromtimestamp(x))



df["20_wk_Moving_Average"] = df["Close"].rolling(window = 140).mean()



fig = go.Figure(data = [go.Candlestick(x=df["Date"], open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"])])


fig.add_trace(go.Scatter(
    x = df["Date"],
    y = df["20_wk_Moving_Average"],
    line = dict(color = "#e0e0e0"),
    name = "20-week Moving Average"
))

fig.update_layout(
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
    yaxis_title = "Apple Price (USD)",
    xaxis_title = "Date"
    )


fig.update_yaxes(type="log")

fig.show()
