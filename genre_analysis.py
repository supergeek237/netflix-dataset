import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def genre_count(df):
    """visualises genre distribution"""
    gen1 = df['listed_in'].str.split(', ')
    gen2 = gen1.explode()

    gen_ct = gen2.value_counts()
        
    print(gen_ct)
        
    return gen_ct

def gen_cor(df):
    """Creates heatmap for release year vs duration"""
    correlation = df[['release_year', 'duration']].corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation of Movie Duration and Release Year')
    plt.tight_layout
    plt.show()

def gen_std(df, gen):
    """calculates std and mean duration for specific gen"""
    get_gen = df.copy()
    get_gen['listed_in'] = get_gen['listed_in'].str.split(', ')
    get_gen = get_gen.explode('listed_in')

    gen_df = get_gen[get_gen['listed_in'] == gen]
    if gen_df.empty:
        print(f"No movies for genre: {gen}")

    dur = gen_df['duration'].to_numpy()
    mean = np.mean(dur)
    std = np.std(dur)
    
    return std, mean
