import pandas as pd
from datetime import datetime

USD_TO_IDR = 16000  

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[df['Title'].str.lower() != 'unknown product']

    df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True)  
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  
    df['Price'] = df['Price'].fillna(0) * USD_TO_IDR  

   
    def parse_rating(rating):
        try:
            return float(rating)
        except:
            match = pd.to_numeric(rating.split('/')[0].strip(), errors='coerce')
            return match if pd.notnull(match) else None

    df['Rating'] = df['Rating'].apply(parse_rating)
    df = df[df['Rating'].notnull()]
    df['Colors'] = df['Colors'].astype(str).str.extract(r'(\d+)')
    df = df[df['Colors'].notnull()]
    df['Colors'] = df['Colors'].astype(int)
    df['Size'] = df['Size'].astype(str).str.strip()
    df['Gender'] = df['Gender'].astype(str).str.strip()
    df['timestamp'] = datetime.now()
    df = df.astype({
        'Title': 'object',
        'Price': 'float64',
        'Rating': 'float64',
        'Colors': 'int64',
        'Size': 'object',
        'Gender': 'object'
    })

    return df