import pandas as pd

def get_departments(df) -> list[str]:

    unique_depart = df['Code INSEE du département'].unique()

    unique_sorted = sorted(unique_depart)

    return list(map(str, unique_sorted))


