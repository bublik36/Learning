import analyse_data as ad
import visualize_data as vd
import get_data as main_data

df = main_data.df()

print(ad.find_static_total(df))

ad.top_five_sold_info(df)

vd.all_graphs(df)
