import matplotlib.pyplot as plt
import get_data as main_data
import numpy as np

data = main_data.df()


def __years_buying(data):
    plt.subplot(3, 1, 1)
    category = np.unique(np.array(data["category"]))
    categoty_quantity_sold = np.zeros(len(category))
    t = 0
    while t < len(category):
        for i in range(len(data)):
            if data.iloc[i, 2] == category[t]:
                categoty_quantity_sold[t] += int(data.iloc[i, 4])
        t += 1
    return category, categoty_quantity_sold


def __total_in_moth(data):
    plt.subplot(3, 1, 2)
    moths = data["date"]
    plt_moths = np.unique([str(np.array(moth[3:-5])) for moth in moths])
    total_money_moth = np.zeros(len(plt_moths))
    t = 0
    while t < len(plt_moths):
        for i in range(len(data)):
            if data.iloc[i, 5][3:-5] == plt_moths[t]:
                total_money_moth[t] += data.iloc[i, 6]
        t += 1
    return plt_moths, total_money_moth


def all_graphs(data):
    fig, ax = plt.subplots(3, 1, figsize=(100, 100))
    ax[0].pie(data["total"], labels=data["product_name"])
    ax[0].set_title("доля предмета в продажах")
    plt_moths, total_money_moth = __total_in_moth(data)
    ax[1].plot(plt_moths, total_money_moth)
    ax[1].set_title("суммарная прибыль по месяцам")
    category, categoty_quantity_sold = __years_buying(data)
    ax[2].bar(category, categoty_quantity_sold)
    ax[2].set_title("суммарные продажи товаров за год")
    plt.show()
