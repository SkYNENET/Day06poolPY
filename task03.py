import pandas as pd

def get_department_prices(df):
    dep_price = df.groupby('Code INSEE du département')['Valeur foncière']
    average_dep = dep_price.mean()
    sort_average_dep = average_dep.sort_index()
    res = sort_average_dep.to_dict()
    print(res)
    

    