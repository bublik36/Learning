import get_data as data
import numpy as np
import asyncio as asyn

_data = data.df()


async def find_static_total(data):
    mean_data = np.mean(np.array(data["total"]))
    median = np.median(np.array(data["total"]))
    despers = np.std(np.array(data["total"]))
    return (
        "\n"
        + "средние значение total: "
        + str(mean_data)
        + "\n"
        + "медиана total: "
        + str(median)
        + "\n"
        + "дисперсия total: "
        + str(despers)
    )


async def top_five_sold_info(data):
    all_solden = np.array(data["quantity_sold"])
    names_solden = np.array(data["product_name"])
    top_five_solden_index = np.argpartition(all_solden, -5)[-5:]
    top_five_solden = all_solden[top_five_solden_index]
    names_solden_top_five = names_solden[top_five_solden_index]
    for i in range(len(top_five_solden_index) - 1, -1, -1):
        if i < len(top_five_solden_index):
            print(
                "\n"
                + str(len(top_five_solden_index) - i)
                + "."
                + " Товар: "
                + str(names_solden_top_five[i])
                + "\n"
                + "его купили: "
                + str(top_five_solden[i])
                + " раз"
            )
