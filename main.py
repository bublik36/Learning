import analyse_data as ad
import visualize_data as vd
import get_data as main_data
import modeling_data as md

df = main_data.df()

print(df)

print(ad.find_static_total(df))

ad.top_five_sold_info(df)

vd.all_graphs(df)

print(md.create_model(df, "Gaming Consoles"))
# вместо камеры можно вписать другое название категории, и по данным, которые отвечают за количество покупок
# данной категории будет выведенно вероятность покупки (например у игровых консолей (Gaming Consoles) больше шанс покупки)
# можно запустить скрипт, и в последней таблице видно, что больше всего покупают и можно отталкиваться от неё
