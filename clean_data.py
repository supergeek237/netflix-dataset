import pandas as pd

def load_data(file_path):
    """Loads the dataset and cleans it"""
    df = pd.read_csv(file_path)
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    df['duration'] = pd.to_numeric(df['duration'].str.replace(' min', ''), errors='coerce')
    df_cleaned = df.dropna(subset=['release_year', 'duration'])
    return df_cleaned
