import pandas as pd

def get_towns(df, department: str | None = None) -> list[dict]:

    if department is None:
        clean_df = df
    else:
        clean_df = df[df['Code INSEE du département'] == department]
    
    if clean_df.empty:
        return []

    towns_list = clean_df[['Nom de la commune', 'Code INSEE de la commune']].drop_duplicates()

    towns_list = towns_list.sort_values('Code INSEE de la commune')
    
    result = [
        {
        "name":row['Nom de la commune'],
        "insee_code": row['Code INSEE de la commune']
        }
        for _, row in towns_list.iterrows()
    ]

    return result
