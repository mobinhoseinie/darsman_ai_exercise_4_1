import pandas as pd


data = pd.read_csv('data.csv')



def standardizer(df: pd.DataFrame):

    # Remove Null Records =======================
    df = df.dropna(how='all')
    # print(df.info())
    
    # Correcting data types =====================
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df = df.fillna(value={
        'Weight' : df['Weight'].mean(),
        'December income' : df['December income'].mean()
    })
    df['Weight'] = df['Weight'].astype('int')
    df['December income'] = df['December income'].astype('int')



    return df








data = standardizer(data)