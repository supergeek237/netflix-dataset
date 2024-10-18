import pandas as pd
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