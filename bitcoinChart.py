#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:49:12 2022

@author: altayavci
"""

from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go
import os

if not os.path.exists("chartgraph"):
    os.mkdir("chartgraph")

cg=CoinGeckoAPI()

bitcoin_data=cg.get_coin_market_chart_by_id(id="bitcoin",vs_currency="usd",days=30)

bitcoin_price_data=bitcoin_data["prices"]

data=pd.DataFrame(bitcoin_price_data,columns=["TimeStamp","Price"])

data["Date"]=pd.to_datetime(data["TimeStamp"],unit="ms")

candlestick_data=data.groupby(data.Date.dt.date).agg({"Price":["min","max","first","last"]})

fig=go.Figure(data=[go.Candlestick(x=candlestick_data.index,
                    open=candlestick_data["Price"]["first"],
                    high=candlestick_data["Price"]["max"],
                    low=candlestick_data["Price"]["min"],
                    close=candlestick_data["Price"]["last"])
                    ])

fig.update_layout(xaxis_rangeslider_visible=False,xaxis_title="Date",yaxis_title="Price (USD)"
                  ,title="Bitcoin Candlestick Chart Over 30 Days")

fig.show()
fig.write_image("chartgraph/fig.png")










