from threading import current_thread
from yfinance import Ticker

# Raw Package
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go


gh = Ticker("GH")
purchase_date_start = "2021-05-17"
purchase_date_end = "2021-11-15"

def get_current_price(ticker):
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

print(get_current_price(gh))

gh_df = yf.download("GH", purchase_date_start, purchase_date_end)

print(gh_df)


cur_min = gh_df['Adj Close'].min()
adjusted_buy = cur_min * .85

print(f"Lowest Price: {cur_min}")
print(f"Adjusted purchase price: {adjusted_buy}")

ax = gh_df['Adj Close'].plot(title="GH's stock price")
ax.axhline(y=cur_min, color='r', linestyle='--', lw=2, label=f"Range Minimum: {cur_min:.2f}")
ax.axhline(y=adjusted_buy, color='b', linestyle='-.', lw=2, label=f"Purchase Price: {adjusted_buy:.2f}")

trans = transforms.blended_transform_factory(
    ax.get_yticklabels()[0].get_transform(), ax.transData)
ax.text(0,cur_min, "{:.2f}".format(cur_min), color="red", transform=trans, 
        ha="right", va="center")
ax.text(0,adjusted_buy, "{:.2f}".format(adjusted_buy), color="blue", transform=trans, 
        ha="right", va="center")
plt.legend(bbox_to_anchor=(0.6,0.4), loc="upper right")
plt.show()