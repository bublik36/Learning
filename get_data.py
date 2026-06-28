import pandas as pd
from datetime import datetime
import numpy as np


def df():
    _df = pd.read_csv("data_shop.csv")
    date_array = np.array(_df["date"])
    _df["date"] = [
        datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y") for date in date_array
    ]
    _df["total"] = _df["price"] * _df["quantity_sold"]
    mean_price = np.full(len(_df), mean_find(_df)).reshape(-1, 1)
    _df["buying_mean"] = np.where(
        np.array(_df["quantity_sold"]).reshape(-1, 1) > mean_price, 1, 0
    )
    _df = _df.fillna(0)
    return _df


def mean_find(data):
    mean_nums = np.mean(np.array(data["quantity_sold"]))
    return mean_nums
