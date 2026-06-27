import pandas as pd
from datetime import datetime
import numpy as np


def df():
    _df = pd.read_csv("data_shop.csv")
    _df = _df.fillna(0)
    date_array = np.array(_df["date"])
    _df["date"] = [
        datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y") for date in date_array
    ]
    _df["total"] = _df["price"] * _df["quantity_sold"]
    print(_df)
    return _df


df()
