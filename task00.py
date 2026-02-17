import pandas as pd

def make_dataframe(path: str):

    df = pd.read_csv(path, sep=';', low_memory=False)

    df_clean = df.dropna(subset=['Latitude', 'Longitude'])

    return df_clean
