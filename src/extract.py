import pandas as pd

def extract_data(file_name):

    df= pd.read_csv(f'data/raw/{file_name}')
    return df
