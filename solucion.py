import pandas as pd

def clean_data(df):
    df.pop('Unnamed: 0')
    df.pop('properati_url')
    df.pop('image_thumbnail')
    df.pop('geonames_id')
    return df

if __name__ == '__main__':

    data = pd.read_csv('properatti.csv')
    dataClean = clean_data(data)
    print(dataClean.head())
    